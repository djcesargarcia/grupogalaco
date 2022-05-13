from operator import le
from django.db import models
from distutils.command.upload import upload
from article.models import Article

# Create your models here.

class Provider(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Name")
    city = models.CharField(max_length=100, verbose_name="City")
    dni = models.CharField(max_length=9, verbose_name="Dni")
    phone_number = models.CharField(max_length=9, verbose_name="Phone Number")
    image = models.ImageField(upload_to='images/', verbose_name='Imagen' ,null=True)
    article_provider = models.ForeignKey(Article, related_name='articles_provider', on_delete=models.CASCADE)
       
    def __str__(self):
        fila = "Name: " + self.name + " - " + "City: " + self.city + " - " + "Dni: " + self.dni + " - " + "Phone Number: " + self.phone_number
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    
    
    