#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import django.utils.timezone as tz
from django.shortcuts import render

from hello.models import Applicant, Requests

logger = logging.getLogger(__name__)


def main_page(request):
    try:
        applicant = Applicant.objects.get(email='jeyzth@gmail.com')
        logger.debug(applicant)
        context = {'applicant': applicant}
        logger.info('Get main_page')
        return render(request, 'hello/index.html', context)
    except:
        logger.info('Empty data in model')
        return render(request, 'hello/emptytable.html', None)


def requests10(request):
    last_requests_list = Requests.objects.order_by('id').reverse()[:10]
    try:
        max_id = last_requests_list[0].id
    except:
        context = {'latest_requests_list': None, 'max_id': None}
    else:    
        context = {'latest_requests_list': last_requests_list, 'max_id': max_id}
    return render(request, 'hello/requests10.html', context)
