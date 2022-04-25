from django.db import models

# Create your models here.

class DriverItem(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    nif = models.CharField(max_length=9, verbose_name='NIF')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    adress = models.CharField(max_length=100, verbose_name='Adress')