from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="Name")
    
    def __str__(self):
        fila = "Name: " + self.name
        return fila