from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,unique=True,primary_key=True)
    profile_picture = models.FileField(upload_to='profiles/')  # uploads to MEDIA_ROOT/profiles/

