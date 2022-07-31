from operator import mod
from unicodedata import name
from django.db import models
from matplotlib.style import context
# from torch import R

# Create your models here.

class SignUp(models.Model):
    username = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    def __str__(self):
        return self.email

class Login(models.Model):
    email = models.EmailField()
    # user = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    password = models.CharField(max_length=120, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email

class Reason(models.Model):
    reason = models.CharField(max_length=120)

    def __str__(self):
        return self.reason

class ContactData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name