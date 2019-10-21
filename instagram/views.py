# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewpostForm,NewProfileForm
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
@login_required(login_url='/accounts/login/')
def addprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            
            profile.save()
        return redirect('viewprofile')

    else:
        form = NewProfileForm
    return render(request, 'profile.html', {"form": form})
@login_required(login_url='/accounts/login/')
def viewprofile(request):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user).first()
    return render(request,'viewprofile.html',{'profile':profile})
# def search_results(request):

#     if 'user' in request.GET and request.GET["user"]:
#         search_term = request.GET.get("user")
#         user = User.search_by_username(search_term)
#         message = f"{search_term}"

#         return render(request, 'all_photos/search.html',{"message":message,"image":images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all_photos/search.html',{"message":message})
def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Image.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})