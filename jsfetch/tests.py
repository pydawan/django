from django.test import TestCase

from django.urls import reverse


class IndexViewTest(TestCase):

    def setUp(self):
        self.url = reverse('jsfetch:index')

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'jsfetch/index.html')

    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
