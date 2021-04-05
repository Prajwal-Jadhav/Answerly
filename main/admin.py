from django.contrib import admin
from .models import Question, Answer, QuestionVote, AnswerVote, QuestionReport, AnswerReport


class QuestionVoteAdmin(admin.ModelAdmin):
    filter_horizontal = ('users_upvoted', 'users_downvoted')


class AnswerVoteAdmin(admin.ModelAdmin):
    filter_horizontal = ('users_upvoted', 'users_downvoted')


class QuestionReportAdmin(admin.ModelAdmin):
    filter_horizontal = 'reporter',


class AnswerReportAdmin(admin.ModelAdmin):
    filter_horizontal = 'reporter',


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionVote, QuestionVoteAdmin)
admin.site.register(AnswerVote, AnswerVoteAdmin)
admin.site.register(QuestionReport, QuestionReportAdmin)
admin.site.register(AnswerReport, AnswerReportAdmin)
