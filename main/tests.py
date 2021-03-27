from django.test import TestCase

from .models import Question
from users.models import User


class QuestionModelTests(TestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(email="abc@gmail.com", first_name="John",
                                         last_name="Smith", PRN="F20111004", year=2, branch="COMP", division="A")

        self.question1 = Question.objects.create(title="A title for question.",
                                                 content="<h1>Hello</h1>", content_markdown="# Hello", asked_by=self.user1)

    def test_question_has_correct_author(self):
        """
        Test if the question has author which was used to create it
        """
        question1 = Question.objects.get(id=self.question1.id)
        user1 = User.objects.get(id=self.user1.id)

        self.assertEqual(question1.asked_by, user1)

    def test_if_question_has_correct_fields_that_were_used_while_creating(self):
        question1 = Question.objects.get(id=self.question1.id)

        self.assertEqual(question1.title, "A title for question.")
        self.assertEqual(question1.content, "<h1>Hello</h1>")
        self.assertEqual(question1.content_markdown, "# Hello")
