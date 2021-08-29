from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, context, loader
from django.views.decorators.csrf import csrf_exempt

from .forms import SignInForm
from .models import Profile

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

@csrf_exempt
def signin(request):
    print('Hello')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(form)
        if form.is_valid():
            profil = form.cleaned_data
            #profil.email = form.user_email
            #profil.password = form.user_password
            print(profil)
            #profil.save()
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        temp = loader.get_template('signin.html')
        return HttpResponse(temp.render())
    