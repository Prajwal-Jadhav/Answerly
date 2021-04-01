from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import QuestionCommentForm
from main.models import Question


@login_required
def create_question_comment(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = QuestionCommentForm(request.POST)

        if form.is_valid():
            # since we are going to add question and author manually we
            # save this form with commit=False
            comment = form.save(commit=False)
            comment.question = question
            comment.author = request.user
            comment.save()

    return redirect(reverse('main:question_details', args=[question_id]))
