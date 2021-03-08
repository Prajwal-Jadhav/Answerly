from django.forms.models import ModelForm

from main.models import Question
from main.models import Answer


class QuestionCreationForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('asked_by', 'created_at', 'votes')


class AnswerCreationForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('answered_by', 'created_at', 'votes')
