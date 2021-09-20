from django.http.response import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, context, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_dj
from django.contrib import messages

from .forms import LogInForm, SignInForm

# Create your views here.
def home(request):
    #temp_home = loader.get_template('home.html')
    #temp_login = loader.get_template('login.html')
    #return HttpResponse(temp.render(context, request))

    if request.user.is_authenticated :
        return render(request, 'blog.html')
    else :
        return HttpResponseRedirect('/login/')

def ideabox(request):
    #temp_home = loader.get_template('home.html')
    #temp_login = loader.get_template('login.html')
    #return HttpResponse(temp.render(context, request))

    if request.user.is_authenticated :
        return render(request, 'ideabox.html')
    else :
        return HttpResponseRedirect('/login/')

def login(request):

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            profil = authenticate(request, username=form.cleaned_data['user_email'], password=form.cleaned_data['user_password'])
            if profil is not None:
                login_dj(request,profil)
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.WARNING, "Sorry it's a bad credentials!")
                return HttpResponseRedirect('/login')
            
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        form = LogInForm()
        return render(request, 'login.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # create new user object
            username=form.cleaned_data['user_username']
            email=form.cleaned_data['user_email']
            password=form.cleaned_data['user_password']

            # if we have same email in database return false
            if User.objects.filter(email=form.cleaned_data['user_email']).count() >= 1 :
                return HttpResponseBadRequest()

            # else create the object
            user = User.objects.create_user(username,email,password)
            user.save()
            return HttpResponseRedirect('/login/')
                
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        form = SignInForm()
        return render(request, 'signin.html', {'form': form})
    