# -*- coding: utf-8 -*-
from os import fork

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


from hello.models import Applicant, Requests


def start_fone_requests():
    pid = fork()
    if (pid == 0):
        return 0
    c = Client()
    for i in range(0, 10):
        c.get(reverse('hello:main_page'))
    exit()


def fill_requests_model():
    for i in range(0, 10):
        r = Requests(
                remote_ip=u"192.168.88.117",
                query_string=u"http://192.168.88.129:8080"
            )
        r.save()


class AppicantTest(TestCase):
    def test_get_mainpage(self):
        """  This test checks how view hard-coded data for the template
             on main page
        """
        c = Client()
        responce = c.get(reverse('hello:main_page'))
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
        response = c.get(reverse('hello:main_page'))
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
        response = c.get(reverse('hello:main_page'))
        self.assertContains(response, u"не знайдено жодного запису")

    def test_correct_view_unicode(self):
        """ This test check correct show unicode data
        """
        c = Client()
        response = c.get(reverse('hello:main_page'))
        ucontent = response.content.decode('utf8')
        self.assertIn(u"9 березня 1973 р.", ucontent)
        self.assertIn(u"Євген", ucontent)
        self.assertIn(u"Анонімов", ucontent)
        self.assertIn(u"Працюю у сфері телекомунікацій", ucontent)
        self.assertIn(u"бажано розробником на Python", ucontent)

    def test_view_requests10(self):
        """  This test checks how view data for the template
                  on requests10 page
        """
        c = Client()
        response = c.get(reverse('hello:requests10'))
        ucontent = response.content.decode('utf8')
        if(ucontent.find(u"table") == -1):
            fill_requests_model()
            response = c.get(reverse('hello:requests10'))
            ucontent = response.content.decode('utf8')
        assert(ucontent.find(u"table") < ucontent.find(u"tbl"))
        for i in range(1, 4):
            assert(ucontent.find(u"-%d" % i) < ucontent.find(
                                                        u"-%d" % (i+1)))
        assert(ucontent.find(u"</tbody>") < ucontent.find(u"</table>"))

    def test_middleware(self):
        """  This test checks:
             How middleware work for add requests.
        """
        # get begin_max_id
        last_requests_list = Requests.objects.order_by('id').reverse()[:10]
        try:
            begin_max_id = last_requests_list[0].id
        except:
            begin_max_id = -1
        # make 10 requestiv
        c = Client()
        for i in range(0, 10):
            c.get(reverse('hello:main_page'))
        last_requests_list = Requests.objects.order_by('id').reverse()[:10]
        current_max_id = last_requests_list[0].id
        print "%d < %d" % (begin_max_id, current_max_id)
        self.assertGreaterEqual(current_max_id - begin_max_id, 10)
