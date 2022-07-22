from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import os
from datetime import datetime

from .forms import LogInForm, NoteForm
from .models import User

# Create your views here.

def index(request):
    user_id = request.session.get("user_id", None)

    if request.method == 'GET':
        # get them to log in
        form = LogInForm(initial = {
            "new_user_id": user_id
        })
        context = {
            "form": form
        }
        return render(request, 'notes/login.html', context)

    elif request.method == 'POST':
        # they want to log in
        form = LogInForm(request.POST)
        if form.is_valid():
            request.session['user_id'] = form.cleaned_data['user_id']
            return HttpResponseRedirect('/notes/notepad') # logged in
        return HttpResponse("Invalid form")
        

def note(request):
    user_id = request.session.get("user_id", None) # retrieve user_id for loggd in user
    if not user_id:
        return HttpResponseRedirect('/notes/')

    user = User.objects.get_or_create(id=user_id)[0] # retrieve user from db [first result]

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