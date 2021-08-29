from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, context, loader

# Create your views here.
def home(request):
    registered = True
    temp_home = loader.get_template('home.html')
    temp_login = loader.get_template('login.html')
    context = {
        'registered': registered,
    }
    #return HttpResponse(temp.render(context, request))
    if registered:
        return HttpResponse(temp_home.render(context, request))
    else :
        return HttpResponse(temp_login.render(context, request))

def login(request):
    temp = loader.get_template('login.html')
    return HttpResponse(temp.render())

def signin(request):
    temp = loader.get_template('signin.html')
    return HttpResponse(temp.render())
