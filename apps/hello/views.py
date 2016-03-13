#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.utils import timezone as tz

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
        context = {'last_requests_list': None, 'max_id': None}
    else:
        context = {'last_requests_list': last_requests_list, 'max_id': max_id}
    return render(request, 'hello/requests10.html', context)

def chknewreq(request):
    logger.info(' -----------    chknewreq --------')
    in_data = request.GET.dict() 
    cur_max_id = int(in_data['cur_max_id'])
    last_requests_list = Requests.objects.order_by('id').reverse()[:10]
    data = {}
    try:
        new_max_id = last_requests_list[0].id
        print "cur=%d new=%d" % (cur_max_id, new_max_id)
    except Exception as e:
        logger.debug('except chknewreq %s\n' % e)
        print "exception"
        return HttpResponse("no data", content_type="application/json")
    data['new_max_id'] = new_max_id    
    if (new_max_id > cur_max_id):
        i = 0
        for req in last_requests_list:
            i = 1 + i
            key = str(i) + "-1"
            data[key] = req.id
            key = str(i) + "-2"
            dt = tz.localtime(req.query_dt)
            sd = "%.2d.%.2d.%.2d %.2d:%.2d:%.2d"
            sd = sd % (dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)
            data[key] = sd
            key = str(i) + "-3"
            data[key] = req.remote_ip
            key = str(i) + "-4"
            data[key] = req.query_string
            key = str(i) + "-5"
            if (req.id > cur_max_id ):
                data[key] = "N"
            else:
                data[key] = "O"
    return HttpResponse(json.dumps(data), content_type="application/json")  # flake8: noqa 
