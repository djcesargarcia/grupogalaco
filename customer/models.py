from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="Name")
    dni = models.CharField(max_length=9, verbose_name="DNI", default="0000000X")
    phone_number = models.CharField(max_length=9, verbose_name="Phone Number", default="00000000")
    postal_code = models.CharField(max_length=5, verbose_name="Postal Code", default="00000")
    
    def __str__(self):
        fila = "Name: " + self.name + " - " + "DNI: " + self.dni + " - " + "Phone Number: " + self.phone_number + "Postal Code: " + self.postal_code + " - " + "Email: " + self.email