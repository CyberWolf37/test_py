from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, context, loader

# Create your views here.
def home(request):
    registered = False
    temp = loader.get_template('home.html')
    context = {
        'registered': registered,
    }
    return HttpResponse(temp.render(context, request))

def login(request):
    temp = loader.get_template('login.html')
    return HttpResponse(temp.render())

def signin(request):
    temp = loader.get_template('signin.html')
    return HttpResponse(temp.render())
