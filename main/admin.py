from django.contrib import admin
from .models import Question, Answer, QuestionVote


class QuestionVoteAdmin(admin.ModelAdmin):
    filter_horizontal = ('users_upvoted', 'users_downvoted')


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionVote, QuestionVoteAdmin)
