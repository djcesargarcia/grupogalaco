from django.db import models

# Create your models here.

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, verbose_name="Name")
    password = models.CharField(max_length=50, verbose_name="Password")
    email = models.CharField(max_length=50, verbose_name="email", default="djcesargarcia@gmail.com")
    confirmation_password = models.CharField(max_length=50, verbose_name="Confirmation Password", default="12345")
    
    def __str__(self):
        fila = "Username " + self.username + " - " + "Password " + self.password + " - " + "Email " + self.email + " - " + "Confirmation Password " + self.confirmation_password
        return fila 
    
    