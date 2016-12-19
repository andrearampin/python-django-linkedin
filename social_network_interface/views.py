from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext


def login(request):
    return render_to_response('social_network_interface/login.html', context=RequestContext(request))


@login_required(login_url='/')
def home(request):
    return render_to_response('social_network_interface/home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')