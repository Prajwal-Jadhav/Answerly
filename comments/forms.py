from django.forms.models import ModelForm

from .models import QuestionComment


# this form will be used to create a comment that is displayed under the question
class QuestionCommentForm(ModelForm):

    class Meta:
        model = QuestionComment
        exclude = ('question', 'author', 'created_at')
