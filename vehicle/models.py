from distutils.command.upload import upload
from fnmatch import translate
from django.db import models
from django.utils.translation import gettext
from driver.models import Driver

# Create your models here.

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    brand = models.CharField(max_length=50, verbose_name='Brand')
    model = models.CharField(max_length=50, verbose_name='Model')
    plate = models.CharField(max_length=9, verbose_name='Plate')
    wheels = models.IntegerField(max_length=1, verbose_name='Wheels')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    driver_vehicle = models.ForeignKey(Driver, related_name='driver_vehicles', on_delete=models.CASCADE, verbose_name='Driver')
  
    def __str__(self):
        fila = "Brand: "+ self.brand + " - " + "Model: " + self.model + " - "+ "Plate: " + self.plate + " - "
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()