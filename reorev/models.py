from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField('created date')
