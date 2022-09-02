from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)