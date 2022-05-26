from tabnanny import verbose
from django.db import models
from distutils.command.upload import upload
 
# Create your models here.

class Zone(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, verbose_name="Name")
    postal_code = models.CharField(max_length=5, verbose_name="Postal Code")
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    city = models.CharField(max_length=50, verbose_name="City")
    population =  models.CharField(max_length=50, verbose_name="Population")
    
    """ Add country and municipality """
    
    def __str__(self):
        fila = "Name: "+ self.name + " - " + "Postal Code: " + self.postal_code + " - " + "City: " + self.city + " - " + "Population: " + self.population
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()