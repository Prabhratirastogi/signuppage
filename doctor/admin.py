from django.contrib import admin

# Register your models here.
from .models import  Contact, Signup, Login
admin.site.register(Contact)
admin.site.register(Signup)
admin.site.register(Login)


