from django import forms

class SignInForm(forms.Form):
    user_email = forms.EmailInput()
    user_password = forms.PasswordInput()