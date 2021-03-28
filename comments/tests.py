from django.test import TestCase

from .models import QuestionComment
from main.models import Question
from users.models import User


class QuestionCommentModelTests(TestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(email="abc@gmail.com", first_name="John",
                                         last_name="Smith", PRN="F20111004", year=2, branch="COMP", division="A")

        self.question1 = Question.objects.create(title="A title for question.",
                                                 content="<h1>Hello</h1>", content_markdown="# Hello", asked_by=self.user1)

        self.question_comment1 = QuestionComment.objects.create(
            content="This is a comment.", question=self.question1, author=self.user1)

    def test_comment_belongs_to_correct_user(self):
        comment = QuestionComment.objects.get(id=self.question_comment1.id)
        user = User.objects.get(id=self.user1.id)

        self.assertEqual(comment.author, user)

    def test_comment_belongs_to_correct_question(self):
        comment = QuestionComment.objects.get(id=self.question_comment1.id)
        question = Question.objects.get(id=self.question1.id)

        self.assertEqual(comment.question, question)
