from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Question(models.Model):
    """
    This class is used to model questions asked by users
    It has a foreign key which corresponds to a user
    """

    title = models.CharField('title for question', max_length=150, blank=False)
    content = models.TextField(
        'more information about question', blank=True, default='')
    content_markdown = models.TextField(null=True)
    asked_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    votes = models.IntegerField('number of votes cast', default=0)

    def __str__(self) -> str:
        return self.title[:60]


class Answer(models.Model):
    """
    This class is used to model answers given by users to particular question.
    It has two foreign keys: 1. Question it belongs to 
                             2. User who wrote it.
    """

    content = models.TextField(blank=False)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.content[:60]
