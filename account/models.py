from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Civil_servant(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null =True)
    name= models.CharField(max_length=100)
    salary = models.IntegerField()
    email=models.EmailField(null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RegistrationData(models.Model):
    name= models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username

