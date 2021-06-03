from django.urls import path

from . import views

app_name = 'moderation'

urlpatterns = [
    path('', views.moderation_home, name='moderation_home'),
    path('reported-questions', views.reported_questions, name='reported_questions')
]
