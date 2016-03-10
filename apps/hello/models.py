# -*- coding: utf-8 -*-
import logging
from django.db import models


logger = logging.getLogger(__name__)


class Applicant(models.Model):
    name = models.CharField(max_length=40, blank=False)
    surname = models.CharField(max_length=40, blank=False)
    dateofbird = models.DateField(blank=False)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=40, unique=True, blank=False)
    jabber = models.EmailField(max_length=40, unique=True, blank=False)
    skype = models.CharField(max_length=40, unique=True, blank=True)
    others = models.TextField(blank=True)

class Requests(models.Model):
   id = models.AutoField("ID", primary_key=True)
   query_dt = models.DateTimeField("Date Time", auto_now_add=True)
   remote_ip = models.IPAddressField("Remote IP", blank=False);
   query_string = models.CharField("Http query", max_length=200);


   