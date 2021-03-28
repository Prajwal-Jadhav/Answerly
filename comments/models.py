from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from ..main.models import Question


class QuestionComment(models.Model):
    """
    This model is used to store the comments that are written for a question.
    """

    # content used to hold the actual text content of the comment. This is the required field.
    content = models.CharField(
        "Write your comment here: ", max_length=350, blank=False, null=False)

    # the question to which this comment belongs to
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=False, null=False)

    # the user who wrote this comment. We get our custom user model through get_user_model()
    # function
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=False, null=False)

    # the time at which this comment was created. We use django's time utility functions so that
    # we can get appropriate timezone
    created_at = models.DateTimeField(default=timezone.now)
