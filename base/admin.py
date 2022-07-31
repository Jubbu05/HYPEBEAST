from django.contrib import admin
from .models import ContactData, SignUp, Login, Reason

# Register your models here.

admin.site.register(Reason)
admin.site.register(ContactData)
admin.site.register(SignUp)
admin.site.register(Login)