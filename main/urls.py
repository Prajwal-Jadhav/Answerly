from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.all_questions, name='all_questions'),
    path('questions/<int:question_id>/',
         views.question_details, name='question_details'),
    path('questions/<int:question_id>/answers/create',
         views.create_answer, name='create_answer'),
    path('questions/<int:question_id>/delete',
         views.delete_question, name='delete_question'),
    path('questions/<int:question_id>/edit',
         views.edit_question, name='edit_question'),
    path('questions/<int:question_id>/answers/<int:answer_id>/delete',
         views.delete_answer, name='delete_answer'),
    path('questions/<int:question_id>/answers/<int:answer_id>/edit',
         views.edit_answer, name='edit_answer'),
    path('questions/new', views.create_question, name='create_question')
]
