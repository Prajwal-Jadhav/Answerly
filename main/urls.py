from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.all_questions, name='all_questions'),
    path('<int:question_id>', views.question_details, name='question_details')
]
