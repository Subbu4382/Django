from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10,unique=True)