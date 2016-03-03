# -*- coding: utf-8 -*-
import sys
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
        self.assertNotIn(u"Алдар", ucontent)
        self.assertNotIn(u"Косе", ucontent)
        self.assertIn(u"9 березня 1973 р.", ucontent)
        self.assertIn(u"jeyzth@gmail.com", ucontent)
        self.assertIn(u"jeyzth@khavr.com", ucontent)
        self.assertNotIn(u"hodzha", ucontent)
        self.assertNotIn(u"nasredin", ucontent)

    def test_page_ws_empty_table(self):
        """ Check no model in the database
        """
        del_rec = Applicant.objects.all()
        del_rec.delete()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        assert(ucontent.find(u"не знайдено жодного запису") > 0)

    def test_correct_view_unicode(self):
        """ This test check correct show unicode data
        """
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        self.assertIn(u"9 березня 1973 р.", ucontent)
        self.assertIn(u"Євген", ucontent)
        self.assertIn(u"Анонімов", ucontent)
        self.assertIn(u"Працюю у сфері телекомунікацій", ucontent)
        self.assertIn(u"бажано розробником на Python", ucontent)

    def test_model_namesakes(self):
        """ Check add few applicant with same Name and Surname
        """
        new_rec1 = Applicant(
            name=u"Алдар",
            surname=u"Косе",
            dateofbird=u"1961-02-09",
            bio="Хитрий і проворний",
            email=u"aldar@satu.kz",
            jabber=u"aldar@xmpp.kz",
            skype=u"aldar.kose",
            others="Хтозна"
        )
        new_rec2 = Applicant(
            name=u"Алдар",
            surname=u"Косе",
            dateofbird=u"1968-02-09",
            bio="Ще біль хитрий і проворний",
            email=u"aldar2@satu.kz",
            jabber=u"aldar2@xmpp.kz",
            skype=u"aldar2.kose",
            others="Хтозна"
        )
        new_rec1.save()
        new_rec2.save()

    def test_model_uniq_fields(self):
        """ Check unique field of model
        """
        new_rec1 = Applicant(
            name=u"Алдар",
            surname=u"Косе",
            dateofbird=u"1961-02-09",
            bio="Хитрий і проворний",
            email=u"aldar4@satu.kz",
            jabber=u"aldar4@xmpp.kz",
            skype=u"aldar4.kose",
            others="Хтозна"
        )
        new_rec2 = Applicant(
            name=u"Алдар",
            surname=u"Косе",
            dateofbird=u"1968-02-09",
            bio="Ще біль хитрий і проворний",
            email=u"aldar4@satu.kz",
            jabber=u"aldar4@xmpp.kz",
            skype=u"aldar4.kose",
            others="Хтозна"
        )
        new_rec1.save()
        try:
            new_rec2.save()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        else:
            print "test fail----------"
            raise
