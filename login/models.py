from django.db import models

# Create your models here.

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, verbose_name="Name")
    password = models.CharField(max_length=50, verbose_name="Password")
    
    def __str__(self):
        fila = "Username " + self.username + " - " + "Password " + self.password
        return fila 