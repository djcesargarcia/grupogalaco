from django.db import models
from article.models import Article

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=100, verbose_name="Description")
    code_buy = models.IntegerField(verbose_name="Code Buy")
    cuantity = models.IntegerField(verbose_name="Cuantity")
    date_buy = models.DateField(auto_now=True)
    date_out = models.DateField(auto_now=True)
    order_article = models.ForeignKey(Article, related_name='articles', on_delete=models.CASCADE)
    
    def __str__(self):
        fila = "Name: " + self.name + " - " + "Description: " + self.description 
        return fila
    