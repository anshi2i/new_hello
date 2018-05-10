# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    html = "<html><body>Hello 1st app</body></html>"
    return HttpResponse(html)
