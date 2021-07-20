from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my hosue !")

def login(request):
    temp = loader.get_template('login.html')
    return HttpResponse(temp.render())
