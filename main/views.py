from django.contrib.auth import login
from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import Answer, Question, QuestionVote
from main.forms import AnswerCreationForm, QuestionCreationForm
import markdown2


def home(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/home.html', {'question_list': question_list})


def all_questions(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/all_questions.html', {'question_list': question_list})


def question_details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()

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
            question.content_markdown = question_content

            question.save()

            QuestionVote.objects.create(question=question)

            return redirect(reverse('main:question_details', args=[question.id]))
    else:
        form = QuestionCreationForm()

    return render(request, 'main/create_question.html', {'form': form})


@login_required
def create_answer(request, question_id):
    if request.method == 'POST':
        form = AnswerCreationForm(request.POST)

        question = get_object_or_404(Question, pk=question_id)

        if form.is_valid():
            # get content of answer in markdown sent by markdown in form
            answer_content_in_markdown = form.cleaned_data['content']

            # convert markdown to html
            answer_content_in_html = markdown2.markdown(
                answer_content_in_markdown)

            answer = form.save(commit=False)
            answer.answered_by = request.user
            answer.question = question

            # save markdown in 'content_markdown' and html in 'content' fields
            answer.content = answer_content_in_html
            answer.content_markdown = answer_content_in_markdown

            answer.save()
            return redirect(reverse('main:question_details', args=[question_id]))

    return redirect(reverse('main:question_details', args=[question_id]))


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if question.asked_by == request.user:
        question.delete()
        messages.success(request, 'Question was successfully deleted.')
    else:
        messages.error(
            request, "You don't have permissions to delete that question")

    return redirect(reverse('main:home'))


@login_required
def delete_answer(request, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    # check only user who wrote above answer is sending request
    if answer.answered_by == request.user:
        answer.delete()
        messages.success(request, 'Answer was successfully deleted.')
        return redirect(reverse('main:question_details', args=[question_id]))
    else:
        messages.error(
            request, "You don't have permissions to delete that answer.")
        return redirect(reverse('main:home'))


@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    # check only user who wrote above question is sending request
    # if not then send unauthorized user to home route
    if request.user != question.asked_by:
        messages.error("You don't have permissions to edit this question.")
        return redirect(reverse('main:home'))

    if request.method == 'POST':
        form = QuestionCreationForm(request.POST, instance=question)
        if form.is_valid():
            question_content_in_markdown = form.cleaned_data['content']
            question = form.save(commit=False)
            question_content_in_html = markdown2.markdown(
                question_content_in_markdown)
            question.content = question_content_in_html
            question.content_markdown = question_content_in_markdown
            question.save()
            return redirect(reverse('main:question_details', args=[question_id]))

    form = QuestionCreationForm(initial={
                                'title': question.title, 'content': question.content_markdown}, instance=question)
    return render(request, 'main/edit_question.html', {'form': form, 'question': question})


@login_required
def edit_answer(request, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    # check only valid user is sending request
    if request.user != answer.answered_by:
        messages.error("You don't have permissions to edit this answer.")
        return redirect(reverse('main:home'))

    if request.method == 'POST':
        form = AnswerCreationForm(request.POST, instance=answer)
        if form.is_valid():
            answer_content_in_markdown = form.cleaned_data['content']
            answer = form.save(commit=False)
            answer_content_in_html = markdown2.markdown(
                answer_content_in_markdown)
            answer.content = answer_content_in_html
            answer.content_markdown = answer_content_in_markdown
            answer.save()
            return redirect(reverse('main:question_details', args=[question_id]))

    form = AnswerCreationForm(
        initial={'content': answer.content_markdown}, instance=answer)

    return render(request, 'main/edit_answer.html', {'form': form, 'question_id': question_id,  'answer_id': answer_id})


@login_required
def vote_question(request, question_id, action):
    question_vote = QuestionVote.objects.get(question__id=question_id)
    upvoting_users = question_vote.users_upvoted.all()
    downvoting_users = question_vote.users_downvoted.all()

    if action == 'up':
        if request.user in upvoting_users:
            pass
        elif request.user in downvoting_users:
            question_vote.users_downvoted.remove(request.user)
            question_vote.users_upvoted.add(request.user)
        else:
            question_vote.users_upvoted.add(request.user)
    elif action == 'down':
        if request.user in upvoting_users:
            question_vote.users_upvoted.remove(request.user)
            question_vote.users_downvoted.add(request.user)
        elif request.user in downvoting_users:
            pass
        else:
            question_vote.users_downvoted.add(request.user)

    question_vote.votes = len(question_vote.users_upvoted.all(
    )) - len(question_vote.users_downvoted.all())

    question_vote.save()

    print(question_vote.votes)
    print(question_vote.users_downvoted.all())
    return JsonResponse({"message": "Successfully voted"})
