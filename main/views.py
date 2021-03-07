from django.shortcuts import render

from .models import Question


def all_questions(request):
    question_list = Question.objects.order_by('-created_at')[:10]

    return render(request, 'main/all_questions.html', {'question_list': question_list})
