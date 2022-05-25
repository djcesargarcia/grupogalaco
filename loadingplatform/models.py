from distutils.command.upload import upload
from fnmatch import translate
from django.db import models

from django.utils.translation import gettext

# Create your models here.

class LoadingPlatform(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=50, verbose_name='Name')
    position = models.IntegerField(max_digits=2)
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    """ Add field vehicle related and consider weight and volumen of load """
        
    def __str__(self):
        fila = "Name: "+ self.name + " - " + "Position: " + self.position
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()