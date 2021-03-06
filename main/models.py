from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class Question(models.Model):
    """
    This class is used to model questions asked by users
    It has a foreign key which corresponds to a user
    """
    title = models.CharField('title for question', max_length=150, blank=False)
    content = models.TextField(
        'more information about question', blank=True, default='')
    asked_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    votes = models.IntegerField('number of votes cast')

    def __str__(self) -> str:
        return self.title[:10] + "..."
