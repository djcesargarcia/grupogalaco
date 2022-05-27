from django.db import models


# Create your models here.

class RoutesDiaries(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Name')

    
    def __str__(self):
        fila = "Name: " + self.name 
        return fila
    
    
    
    
