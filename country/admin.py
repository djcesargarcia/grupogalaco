from django.contrib import admin

# Register your models here.
from .models import Country

admin.site.register(Country)

class countryAdmin(admin.ModelAdmin):
   list_display=['continent','country']


