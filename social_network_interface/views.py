from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext


def login(request):
    context = RequestContext(request, {'user': request.user})
    return render_to_response('social_network_interface/login.html', context=context)


@login_required(login_url='sni:login')
def home(request):
    context = RequestContext(request, {'user': request.user})
    return render_to_response('social_network_interface/home.html', context=context)


def logout(request):
    auth_logout(request)
    return redirect('sni:login')