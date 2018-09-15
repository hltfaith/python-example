from django.db import models

# Create your models here.

class asset_db(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    ip_addr = models.CharField(max_length=32)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    sn = models.CharField(max_length=32)
    local = models.CharField(max_length=32)
    resource_type = models.CharField(max_length=32)
    port = models.DecimalField(max_digits=8,decimal_places=0)
    system_version = models.CharField(max_length=32)
    group = models.CharField(max_length=16)
