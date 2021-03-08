from django.forms.models import ModelForm

from main.models import Question


class QuestionCreationForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('asked_by', 'created_at', 'votes')
