from django.db import models

# Create your models here.

class LoadLorry(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    volume = models.DecimalField(max_digits=5, decimal_places=3)
    mma = models.DecimalField(max_digits=5, decimal_places=3)
    tare = models.DecimalField(max_digits=5, decimal_places=3)
    cuantity = models.DecimalField(max_digits=5, decimal_places=3)
    empty_weight = models.DecimalField(max_digits=5, decimal_places=3)
    total_weight = models.DecimalField(max_digits=5, decimal_places=3)
    
    def __str__(self):
        fila = "Id: " + self.id + " - " + "Weight: " + self.weight + " - " + "Volume: " + self.volume + " - " + "MMA: " + self.mma + " - " + "Cuantity: " + self.cuantity + " - " + "Tare: " + self.tare + " - " + "Empty Weight: " + self.empty_weight + " - " + "Total Weight: " + self.total_weight
        return fila
    
    """ Consider vehicle as related field and articles and driver """
     
