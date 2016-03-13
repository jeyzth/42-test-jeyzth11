# -*- coding: utf-8 -*-
import logging


from hello.models import Requests

logger = logging.getLogger(__name__)


class SaveRequest(object):
    def process_request(self, request):
        d = {}
        rh = request.method
        if rh == 'GET':
            d = request.GET.dict()
        if rh == 'POST':
            d = request.POST.dict()
        s = str(d)
        z = request.path
        try:
            i = z.index('requests10')
            if i >= 0:
                return None
        except:
            i = 0

        try:
            i = z.index('chknewreq')
            if i >= 0:
                return None
        except:
            i = 0

        ip_s = request.META["REMOTE_ADDR"]
        logger.debug('-->middleware URL='+z+'|' + request.META["REMOTE_ADDR"])
        new_req = Requests(
            remote_ip=ip_s,
            query_string="URL="+z+"Data="+s
            )
        new_req.save()
        return None
