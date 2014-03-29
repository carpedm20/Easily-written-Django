# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def write_post(request):
    return HttpResponse("장고 어렵지 아니해")
