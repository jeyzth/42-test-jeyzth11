# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    try:
        return render(request, 'hello/index.html', None)
    except:
        return render(request, 'hello/emptytable.html', None)
