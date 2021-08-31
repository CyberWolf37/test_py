from django import forms
from django.forms import ModelForm

class SignInForm(forms.Form):
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label="Email address")
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label="Password")

class LogInForm(forms.Form):
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label="Email address")
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label="Password")