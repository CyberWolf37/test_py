from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(max_length=200)
    passord = models.CharField(max_length=100)
