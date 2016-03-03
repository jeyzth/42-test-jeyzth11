# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client


from hello.models import Applicant


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

    def test_siggle_record(self):
        """ This test show one entry , even if in a few.
             Add fake aplikants
        """
        new_rec1 = Applicant(
            name=u"Алдар",
            surname=u"Косе",
            dateofbird=u"1968-02-09",
            bio="Хитрий і проворний",
            email=u"aldar@satu.kz",
            jabber=u"aldar@xmpp.kz",
            skype=u"aldar.kose",
            others="Хтозна"
        )
                                                                                                                
        new_rec3 = Applicant(
            name=u"Ходжа",
            surname=u"Насрідін",
            dateofbird=u"1963-07-04",
            bio="Дуже язикатий",
            email=u"hodzha@satu.uz",
            jabber=u"hodzha@xmpp.uz",
            skype=u"hodzha.nasredin",
            others="Дезна"
        )
        new_rec1.save()
        new_rec3.save()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        self.assertNotIn(u"Алдар",ucontent)
        self.assertNotIn(u"Косе",ucontent)
        self.assertIn(u"9 березня 1973 р.",ucontent)
        self.assertIn(u"jeyzth@gmail.com",ucontent)
        self.assertIn(u"jeyzth@khavr.com",ucontent)
        self.assertNot(u"hodzha",ucontent)
        self.assertNotIn(u"nasredin",ucontent)
