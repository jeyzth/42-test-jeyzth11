from django.test import TestCase
from django.test.client import Client


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class AppicantTest(TestCase):
    def test_get_mainpage(self):
        """  This test checks how view hard-coded data for the template
             on main page
        """
        c = Client()
        responce = c.get('http://localhost:8080')
        s = responce.content
        self.assertIn("42 Coffee Cups Test Assignment", s)
        self.assertIn("Contacts", s)
        self.assertIn("Email:", s)
        self.assertIn("Jabber:", s)
        self.assertIn("Skype:", s)
        self.assertIn("Other contacts:", s)
        self.assertIn("Bio:", s)
