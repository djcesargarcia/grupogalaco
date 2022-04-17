from django.db import models

# Create your models here.

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Name')
    nif = models.CharField(max_length=9, verbose_name='NIF')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    adress = models.CharField(max_length=100, verbose_name='Adress')

    def __str__(self):
        fila = "Name: "+ self.name + " - " + "NIF: " + self.nif + " - " + "Adress: " + self.adress
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
        
