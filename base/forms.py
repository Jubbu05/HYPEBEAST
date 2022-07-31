from dataclasses import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactData, SignUp

class ContactForm(ModelForm):
    class Meta:
        model = ContactData
        fields = '__all__'
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control bg-dark text-white', 'id': 'exampleFormControlInput1', 'placeholder': 'Enter your Name', 'name':'name'}),

            'phone': widgets.NumberInput(attrs={'class': 'form-control bg-dark text-white', 'id': 'phone', 'placeholder': 'Enter your Phone Numbe', 'name':'phone'}),

            'email': widgets.TextInput(attrs={'class': 'form-control bg-dark text-white', 'id': 'exampleFormControlInput2', 'placeholder': 'Enter your Email address', 'name':'address'}),

            'reason': widgets.Select(attrs={'class': 'form-control bg-dark text-muted my-2', 'id': 'exampleFormControlSelect1', 'name':'reason'}),

            'message': widgets.Textarea(attrs={'class': 'form-control bg-dark text-white', 'id': 'exampleFormControlTextarea1', 'placeholder': 'Please tell us more about the reason for your enquiry', 'name':'message'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1','name':'user_name'}),

            'email': widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1','aria-describedby': 'emailHelp', 'name':'email'}),

            'password1': widgets.PasswordInput(attrs={'class': 'form-control', 'id': 'cexampleInputPassword1', 'name':'password'}),

            'password1': widgets.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputPassword1', 'name':'confirm_password'}),
        }
