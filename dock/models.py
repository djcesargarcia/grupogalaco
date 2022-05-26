from tabnanny import verbose
from django.db import models
from distutils.command.upload import upload
 
# Create your models here.

class Dock(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, verbose_name="Name")
    position = models.CharField(max_length=1, verbose_name="Position")
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    
    def __str__(self):
        fila = "Name: "+ self.name + " - " + "Position: " + self.position
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()