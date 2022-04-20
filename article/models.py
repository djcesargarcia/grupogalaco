from django.db import models
from django.forms import CharField

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, verbose_name="Name")
    weight = models.CharField(max_length=5, verbose_name="Weight") 
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        fila = "Name: "+ self.name + " - " + "Weight: " + self.weight + " - " + "Qrcode: " + self.image + " - " + "Price: " + self.price
        return fila