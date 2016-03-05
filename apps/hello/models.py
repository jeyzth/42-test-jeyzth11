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
