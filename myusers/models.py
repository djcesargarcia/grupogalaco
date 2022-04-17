from django.db import models

# Create your models here.

class Myusers(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Name")
    surname = models.CharField(max_length=50, verbose_name="Surname")
    population = models.CharField(max_length=50, verbose_name="Population")
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    nif = models.CharField(max_length=9, verbose_name="NIF")
    
    def __str__(self):
        fila = "Name: "+ self.name +  " - " + "Surname: "+ self.name +  " - " + "Population: "+ self.name +  " - " + "NIF: "+ self.name 
        return fila 
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
