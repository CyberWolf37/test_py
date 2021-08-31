from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, context, loader
from django.views.decorators.csrf import csrf_exempt

from .forms import LogInForm, SignInForm
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
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            profil = Profile.objects.filter(email=form.cleaned_data['user_email'], password=form.cleaned_data['user_password'])
            if profil.count() == 1:
                 return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login/')
            
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        form = LogInForm(request.POST)
        return render(request, 'login.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            profil = Profile.create(email=form.cleaned_data['user_email'],password=form.cleaned_data['user_password'])
            profil.save()
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        form = SignInForm()
        return render(request, 'signin.html', {'form': form})
    