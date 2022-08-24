from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import os
from datetime import datetime

import sys
import Authwave

import django.shortcuts

# Create your views here.

def index(request):
    currentUri = request.get_host() + request.get_full_path()
    authenticator = Authwave.Authenticator(b'11111111111111111111111111111111', currentUri, request.session, django.shortcuts, "https://test.login.authwave.com/")

    if request.method == 'GET':
        if authenticator.isLoggedIn():
            return HttpResponseRedirect('/notes/notepad') # logged in
        else: 
            return HttpResponseRedirect('/notes')
        
