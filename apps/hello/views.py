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
        applicant = Applicant.objects.first()
        logger.debug(applicant)
        context = {'applicant': applicant}
        logger.info('Get main_page')
        return render(request, 'hello/index.html', context)

def requests_page(request):
    last_requests_list = Requests.objects.order_by('-id')[:10]
    if last_requests_list :
        max_id = int(last_requests_list[0].id)
    else:
        max_id = None
    context = {'last_requests_list': last_requests_list, 'max_id': max_id}
    return render(request, 'hello/requests_page.html', context)

def chknewreq(request):
    logger.info(' -----------    chknewreq --------')
    in_data = request.GET.dict() 
    print in_data
    cur_max_id = int(in_data['cur_max_id'])
    last_requests_list = Requests.objects.order_by('id').reverse()[:10]
    data = {}
    try:
        new_max_id = int(last_requests_list[0].id)
        print "cur=%d new=%d" % (cur_max_id, new_max_id)
    except Exception as e:
        # logger.debug('except chknewreq %s\n' % e)
        print "exception"
        data['error']= "no data"
        data['new_max_id'] = -1
        return HttpResponse(json.dumps(data), content_type="application/json")
    data['new_max_id'] = new_max_id    
    if (new_max_id > cur_max_id):
        i = 0
        for req in last_requests_list:
            i = 1 + i
            data[str(i) + "-1"] = req.id
            dt = tz.localtime(req.query_dt)
            data[str(i) + "-2"] = dt.strftime("%d.%m.%Y %H:%M:%S")
            data[str(i) + "-3"] = req.remote_ip
            data[str(i) + "-4"] = req.query_string
            if (req.id > cur_max_id ):
                data[str(i) + "-5"] = "N"
            else:
                data[str(i) + "-5"] = "O"
    return HttpResponse(json.dumps(data), content_type="application/json")  # flake8: noqa 
