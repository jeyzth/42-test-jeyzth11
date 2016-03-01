# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from hello.models import Applicant


def index(request):
    try:
        applicant = Applicant.objects.get(email = 'jeyzth@gmail.com')
        context = {'applicant': applicant}
        return render(request, 'hello/index.html', context)
    except:
        return render(request, 'hello/emptytable.html', None)
