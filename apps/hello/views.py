#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import django.utils.timezone as tz
from django.shortcuts import render

from hello.models import Applicant

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
    last_requests_list = list()
    for i in range(0, 10):
        print i
        last_requests_list.append({'id': i, 'query_dt': tz.now(),
                                   'remote_ip': '192.168.88.1',
                                   'query_string': 'http://192.168.88.129:8080'
                                   })
        time.sleep(0.1)
    max_id = int(last_requests_list[9]['id'])
    context = {'last_requests_list': last_requests_list, 'max_id': max_id}
    return render(request, 'hello/requests10.html', context)
