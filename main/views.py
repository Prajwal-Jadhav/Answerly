from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Question
from main.forms import QuestionCreationForm


def home(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/home.html', {'question_list': question_list})


def all_questions(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/all_questions.html', {'question_list': question_list})


def question_details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('question does not exists.')

    return render(request, 'main/question_details.html', {'question': question})


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asked_by = request.user
            question = question.save()
            redirect(reverse('main:question_details', args=[question.id]))
    else:
        form = QuestionCreationForm()

    return render(request, 'main/create_question.html', {'form': form})
