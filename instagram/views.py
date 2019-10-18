# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http  import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')

def welcome(request):
    return render(request, 'welcome.html')

# @login_required(login_url='/accounts/login/')
# def image(request, image_name):