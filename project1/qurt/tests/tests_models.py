from django.test import TestCase
from  qurt.forms import TraditionForm
from ..models import * 
class MethodTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Facts.objects.create(importantyears='123', conclusion='dsdsdsd')


    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertFalse(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test_valid_form(self):
       print("Method: test_valid_form")
       w = Facts.objects.create(importantyears='123', conclusion='Footer')
       data = {'conclusion': w.conclusion,}
       form = TraditionForm(data=data)
       self.assertTrue(form.is_valid())

    
 
