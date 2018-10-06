from django.db import models

# Create your models here.


class Book(models.Model):
     id=models.AutoField(primary_key=True)
     title=models.CharField(max_length=32,unique=True)
     pub_date=models.DateField()
     price=models.DecimalField(max_digits=8,decimal_places=2) # 999999.99
     publish=models.CharField(max_length=32)

     def __str__(self):
         return self.title


