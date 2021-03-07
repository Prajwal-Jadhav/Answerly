from django.http.response import Http404
from django.shortcuts import render

from .models import Question


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
