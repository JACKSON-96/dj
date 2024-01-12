from django.test import TestCase, Client
from django.urls import reverse

class MyViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('my_view_name'))
        self.assertEqual(response.status_code, 200)
