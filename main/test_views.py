from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):

    def test_home_page_is_accessable(self):
        response = self.client.get(reverse('main:home'))

        self.assertEqual(response.status_code, 200)

    def test_query_set_is_empty(self):
        """When there are no questions in database queryset should be empty"""

        response = self.client.get(reverse('main:home'))

        self.assertQuerysetEqual(
            response.context['question_list'], [])
