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
    path('questions/new', views.create_question, name='create_question')
]
