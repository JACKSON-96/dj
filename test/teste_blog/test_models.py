from django.test import TestCase
from apps.models import reverse

class MyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        apps.objects.create(name='Test')

    def test_model_name(self):
        model = apps.objects.get(id=1)
        expected_object_name = f'{model.name}'
        self.assertEqual(expected_object_name, 'Test')
