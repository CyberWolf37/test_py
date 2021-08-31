from django.db import models
from .forms import SignInForm

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    @classmethod
    def create(cls, email, password):
        profil = cls(email=email, password=password)
        # do something with the book
        return profil
