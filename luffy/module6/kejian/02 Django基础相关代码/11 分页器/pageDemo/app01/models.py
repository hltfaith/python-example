from django.db import models

# Create your models here.



class  Book(models.Model):

    title=models.CharField(max_length=32)
    price=models.DecimalField(decimal_places=2,max_digits=8)
