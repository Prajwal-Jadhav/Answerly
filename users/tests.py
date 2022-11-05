# Create your tests here.

from django.contrib.auth.models import User
from django.test import TestCase, Client

class RegisterTest(TestCase):

    def test_user_registration(self):
        client = Client()

        response = client.post("/register", dict(email = "prajwal@gmail.com", first_name = "John",
        last_name = "Doe", PRN = "F19112005", year = 4, branch = "COMP", division = "B", password = "testing321"),
        follow=True)

        assert response.status_code == 200


# class LoginTest(TestCase):
#     real_user = {"username": "jadhavv933@gmail.com", "password": "postgres"}
#     fake_user = {"username": "fake@gmail.com", "password": "password"}


#     def setUp(self) -> None:
#         client = Client()

#         response = client.post("/register", dict(email = "jadhavv933@gmail.com", first_name = "John",
#         last_name = "Doe", PRN = "F19112005", year = 4, branch = "COMP", division = "B", password = "postgres"),
#         follow=True)


#     def test_login_real_user(self):
#         # send login data
#         response = self.client.post('/login', self.real_user, follow=True)
#         # should be logged in now
#         self.assertTrue(response.context['user'].is_active)

