#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render

from hello.models import Applicant

logger = logging.getLogger(__name__)


def main_page(request):
        applicant = Applicant.objects.first()
        logger.debug(applicant)
        context = {'applicant': applicant}
        logger.info('Get main_page')
        return render(request, 'hello/index.html', context)
