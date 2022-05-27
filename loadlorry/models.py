from django.db import models

# Create your models here.

class LoadLorry(models.Model):
    id = models.Autofield(primary_key=True, verbose_name="ID")
    weight = models.FloatField(max_digits=2, verbose_name="Weight")
    volume = models.FloatField(max_digits=2, verbose_name="Volume")
    mma = models.FloatField(max_digits=2, verbose_name="MMA")
    tare = models.FloatField(max_digits=2, verbose_name="Tare")
    cuantity = models.FloatField(max_digits=2, verbose_name="Cuantity")
    empty_weight = models.FloatField(max_digits=2, verbose_name="Empty Weight")
    total_weight = models.FloatField(max_digits=2, verbose_name="Total Weight")
    
    def __str__(self):
        fila = "Id: " + self.id + " - " + "Weight: " + self.weight + " - " + "Volume: " + self.volume + " - " + "MMA: " + self.mma + " - " + "Cuantity: " + self.cuantity + " - " + "Tare: " + self.tare + " - " + "Empty Weight: " + self.empty_weight + " - " + "Total Weight: " + self.total_weight
        return fila
    
    """ Consider vehicle as related field and articles and driver """
     
