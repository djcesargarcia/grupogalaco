from django.db import models

# Create your models here.

class LoadLorry(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    weight = models.FloatField(verbose_name="Weight")
    volume = models.FloatField(verbose_name="Volume")
    mma = models.FloatField(verbose_name="MMA")
    tare = models.FloatField(verbose_name="Tare")
    cuantity = models.FloatField(verbose_name="Cuantity")
    empty_weight = models.FloatField(verbose_name="Empty Weight")
    total_weight = models.FloatField(verbose_name="Total Weight")
    
    def __str__(self):
        fila = "Id: " + self.id + " - " + "Weight: " + self.weight + " - " + "Volume: " + self.volume + " - " + "MMA: " + self.mma + " - " + "Cuantity: " + self.cuantity + " - " + "Tare: " + self.tare + " - " + "Empty Weight: " + self.empty_weight + " - " + "Total Weight: " + self.total_weight
        return fila
    
    """ Consider vehicle as related field and articles and driver """
     
