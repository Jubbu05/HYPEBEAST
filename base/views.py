from cmath import log
import email
import re
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import ContactData
from .forms import ContactForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# def loginUser(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(email=email)
#         except:
#             messages.error(request, 'User does not exist')
           
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, 'Email address or Password does not exist')
#     context = {}
#     return render(request, 'base/index.html', context)

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'base/login.html', context)

def SignUpUser(request):
    form1 = CreateUserForm()

    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('login')

    context = {'form1': form1}
    return render(request, 'base/signup.html', context)


def index(request):
    context = {}
    return render(request, 'base/index.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def contact(request):
    n=''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            n = 'Thank you for your enquiry. We will get back to you soon.'
    context = {'form': form, 'n': n}
    return render(request, 'base/contact.html', context)
