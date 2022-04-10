from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


class Signup(models.Model):
    msg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=100)
    img=models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=100)
    passs1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Login(models.Model):
    username = models.CharField(max_length=50)
    passs1 = models.CharField(max_length=50)

    def __str__(self):
        return self.username




   


   




    





