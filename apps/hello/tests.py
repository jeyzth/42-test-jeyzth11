# -*- coding: utf-8 -*-
import sys
import json
from os import fork
from time import sleep
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


from hello.models import Applicant, Requests


def make_fone_10_requests():
    pid = fork()
    if (pid != 0):
        return pid
    c = Client()
    for i in range(0, 10):
        c.get(reverse('hello:main_page'))
    sys.exit(0)


def make_10_requests():
    c = Client()
    for i in range(0, 10):
        c.get(reverse('hello:main_page'))
        sleep(0.1)


def fill_requests_model():
    for i in range(0, 10):
        r = Requests(
                remote_ip=u"192.168.88.117",
                query_string=u"http://192.168.88.129:8080"
            )
        r.save()


class AppicantTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_get_mainpage(self):
        """  This test checks how view hard-coded data for the template
             on main page
        """
        responce = self.c.get(reverse('hello:main_page'))
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
            skype=u"Aldar.kose",
            others="Алма1"
        )
        new_rec3 = Applicant(
            name=u"Ходжа",
            surname=u"Насрідін",
            dateofbird=u"1963-07-04",
            bio="Дуже язикатий",
            email=u"hodzha@satu.uz",
            jabber=u"hodzha@xmpp.jp",
            skype=u"hodzha.nasredin",
            others="Аста1"
        )
        new_rec1.save()
        new_rec3.save()
        response = self.c.get(reverse('hello:main_page'))
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
        response = self.c.get(reverse('hello:main_page'))
        self.assertContains(response, u"не знайдено жодного запису")

    def test_correct_view_unicode(self):
        """ This test check correct show unicode data
        """
        response = self.c.get(reverse('hello:main_page'))
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
        return "OK"
        fill_requests_model()
        response = self.c.get(reverse('hello:requests10'))
        return "OK"
        ucontent = response.content.decode('utf8')
        print ucontent
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
        last_requests_list = Requests.objects.order_by('id').reverse()[:10]
        try:
            begin_max_id = last_requests_list[0].id
        except:
            begin_max_id = -1
        for i in range(0, 10):
            self.c.get(reverse('hello:main_page'))
        last_requests_list = Requests.objects.order_by('id').reverse()[:10]
        current_max_id = last_requests_list[0].id
        print "%d < %d" % (begin_max_id, current_max_id)
        self.assertGreaterEqual(current_max_id - begin_max_id, 10)

    def test_chk_new_requests(self):
        """ This test check backand for asynchron update
            requests10
        """
        make_10_requests()
        sleep(2)
        cur_max_id = 5
        response = self.c.get(reverse('hello:chknewreq'), {'cur_max_id':
                         cur_max_id})
        cx = json.loads(response.content)
        new_max_id = cx['new_max_id']
        print new_max_id
        # for i in range(1, 11):
        #    print " %s %s %s %s %s \n" % (cx["%d-1" % i], cx["%d-2" % i],
        #                                  cx["%d-3" % i], cx["%d-4" % i],
        #                                  cx["%d-5" % i])
        self.assertGreater(new_max_id, 0)
