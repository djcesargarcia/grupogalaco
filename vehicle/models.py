from distutils.command.upload import upload
from fnmatch import translate
from django.db import models
from routes.models import Routes
from django.utils.translation import gettext

# Create your models here.

class Vehicule(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    brand = models.CharField(max_length=50, verbose_name='Brand')
    model = models.CharField(max_length=50, verbose_name='Model')
    plate = models.CharField(max_length=9, verbose_name='Plate')
    wheels = models.IntegerField(max_digits=1, verbose_name='Wheels')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    adress = models.CharField(max_length=100, verbose_name='Adress')
  
    def __str__(self):
        fila = "Name: "+ self.brand + " - " + "NIF: " + self.nif + " - " + "Adress: " + self.adress
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()