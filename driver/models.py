from distutils.command.upload import upload
from django.db import models
from routes.models import Routes

# Create your models here.

class Driver(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=50, verbose_name='Name')
    nif = models.CharField(max_length=9, verbose_name='NIF')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    adress = models.CharField(max_length=100, verbose_name='Adress')
    driver_routes = models.ForeignKey(Routes, related_name='routes',on_delete=models.CASCADE)

    def __str__(self):
        fila = "Name: "+ self.name + " - " + "NIF: " + self.nif + " - " + "Adress: " + self.adress
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()