from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my hosue !")

def login(request):
    return HttpResponse(loader.select_template('reorev/html_file/login.html').render())
