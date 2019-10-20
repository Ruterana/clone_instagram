# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewpostForm
from  .models import Image,Profile
from django.http  import HttpResponse


@login_required(login_url='/accounts/login/')
def welcome(request):
    images=Image.objects.all()
    return render(request,'welcome.html',{ 'images':images})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewpostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            
            image.save()
        return redirect('welcome')

    else:
        form = NewpostForm()
    return render(request, 'new_post.html', {"form": form})
