from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('question/<int:question_id>/create',
         views.create_question_comment, name='create_question_comment')
]
