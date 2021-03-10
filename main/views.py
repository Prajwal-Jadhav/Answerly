from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import Answer, Question
from main.forms import AnswerCreationForm, QuestionCreationForm
import markdown2


def home(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/home.html', {'question_list': question_list})


def all_questions(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/all_questions.html', {'question_list': question_list})


def question_details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        answers = question.answer_set.all()
    except Question.DoesNotExist:
        raise Http404('question does not exists.')

    form = AnswerCreationForm()

    return render(request, 'main/question_details.html', {'question': question, 'answers': answers, 'form': form})


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            question_content = form.cleaned_data['content']
            content_in_html = markdown2.markdown(question_content)
            question = form.save(commit=False)
            question.asked_by = request.user
            question.content = content_in_html
            question.save()
            return redirect(reverse('main:question_details', args=[question.id]))
    else:
        form = QuestionCreationForm()

    return render(request, 'main/create_question.html', {'form': form})


@login_required
def create_answer(request, question_id):
    if request.method == 'POST':
        form = AnswerCreationForm(request.POST)
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404(
                'The question you are trying to answer does not exists.')

        if form.is_valid():
            answer = form.save(commit=False)
            answer.answered_by = request.user
            answer.question = question
            answer.save()
            return redirect(reverse('main:question_details', args=[question_id]))

    return redirect(reverse('main:question_details', args=[question_id]))


@login_required
def delete_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('The question you are trying to answer does not exists.')

    if question.asked_by == request.user:
        question.delete()
        messages.success(request, 'Question was successfully deleted.')
    else:
        messages.error(
            request, "You don't have permissions to delete that question")

    return redirect(reverse('main:home'))
