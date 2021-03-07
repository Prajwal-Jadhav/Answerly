from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.all_questions, name='all_questions')
]
