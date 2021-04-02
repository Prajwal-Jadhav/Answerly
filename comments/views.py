from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .forms import QuestionCommentForm
from main.models import Question
from .models import QuestionComment


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


@login_required
def delete_question_comment(request, comment_id):
    comment = get_object_or_404(QuestionComment, id=comment_id)

    # id of the question to which target comment belongs to so that we can
    # use it to redirect to question_details page
    question_id = comment.question.id

    # only the user who wrote comment can delete it
    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Successfully deleted the comment.")
    else:
        messages.error(
            request, "You don't have the permission to delete that comment.")

    return redirect(reverse("main:question_details", args=[question_id]))
