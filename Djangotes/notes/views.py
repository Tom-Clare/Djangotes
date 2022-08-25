from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import os
from datetime import datetime

import sys
import Authwave

from .forms import LogInForm, NoteForm
from .models import User

import django.shortcuts

# Create your views here.

def index(request):
    user_id = request.session.get("user_id", None)

    authenticator = Authwave.Authenticator(b'11111111111111111111111111111111', request.build_absolute_uri(), request.session, django.shortcuts, "https://test.login.authwave.com/")

    if request.method == 'GET':
        if authenticator.isLoggedIn():
            return HttpResponseRedirect('/notes/notepad')

        form = LogInForm(initial = {
            "new_user_id": user_id
        })
        context = {
            "form": form
        }
        return render(request, 'notes/login.html', context)

def login(request):
    authenticator = Authwave.Authenticator(b'11111111111111111111111111111111', request.build_absolute_uri(), request.session, django.shortcuts, "https://test.login.authwave.com/")
    if authenticator.isLoggedIn() == True:
            return HttpResponseRedirect('/notes/notepad')
    else:
        return authenticator.login()


def logout(request):
    authenticator = Authwave.Authenticator(b'11111111111111111111111111111111', request.build_absolute_uri(), request.session, django.shortcuts, "https://test.login.authwave.com/")
    authenticator.logout()

    return HttpResponseRedirect('/notes/') # log in screen

def note(request):
    authenticator = Authwave.Authenticator(b'11111111111111111111111111111111', request.build_absolute_uri(), request.session, django.shortcuts, "https://test.login.authwave.com/")
    if authenticator.isLoggedIn() == False:
        return HttpResponseRedirect('/notes/')

    user = User.objects.get_or_create(id=authenticator._user.id)[0] # retrieve user from db [first result]

    if request.method == 'GET':
        notetext = user.text
        
        # pre-populate form
        form = NoteForm(initial={
            'notetext': notetext
        })

        context = {
            "form": form
        }
        return render(request, 'notes/note.html', context)

    elif request.method == 'POST':
        # they're giving us new data, we need to update the db with it
        match request.POST.get("auth"):
            case "logout":
                #logout
                request.session.flush()
                return HttpResponseRedirect("/notes/notepad")

            # unset
        form = NoteForm(request.POST)
        if form.is_valid():
            # process form data
            user.text = form.cleaned_data['notetext']
            user.save()
        return HttpResponseRedirect("/notes/notepad")