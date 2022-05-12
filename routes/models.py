from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Routes(models.Model):
    id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=50, verbose_name="Place")
    origin = models.CharField(max_length=50, verbose_name="Origin")
    destiny = models.CharField(max_length=50, verbose_name="Destiny")
    postal_code = models.CharField(max_length=50, verbose_name="Postal Code")
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)

    
    def __str__(self) -> str:
        fila = "Place: " + self.place + " - " + "Origin: " + self.origin + " - " + "Destiny: " + self.destiny + " - " + "Postal Code: " + self.postal_code
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


