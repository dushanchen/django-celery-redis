# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

from celerytest import celery_app

import time
import datetime

@celery_app.task
def log(info):
    time.sleep(10)
    print(info)



def index(request):
    for i in range(100):
        log.delay('hello,dsc---%s' % (i))
    return JsonResponse({'now':datetime.datetime.now().strftime('%Y%m%d %H:%M%S')})