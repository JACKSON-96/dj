from django.test import TestCase
from myapp.forms import MyForm

class MyFormTest(TestCase):
    def test_form_validity(self):
        form_data = {'field1': 'value1', 'field2': 'value2'}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())
