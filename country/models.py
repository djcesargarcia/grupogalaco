
from django.db import models

class Country(models.Model):
    
    country = models.CharField(max_length=256, verbose_name='country')
    continent = models.CharField(max_length=64, verbose_name='continent')
    
    def __str__(self) -> str:
        fila = "Country: " + self.country + " - " + "Continent: " + self.continent
        return fila
    


