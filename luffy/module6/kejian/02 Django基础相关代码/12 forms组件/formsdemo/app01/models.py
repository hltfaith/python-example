from django.db import models

# Create your models here.



class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    email=models.EmailField()
    tel=models.CharField(max_length=32)