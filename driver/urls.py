from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros',views.nosotros, name="nosotros"),
    path('drivers/',views.drivers, name="drivers"),
    path('drivers/create',views.create_drivers, name="create_drivers"),
    path('drivers/edit',views.edit_drivers, name="edit_drivers"),
    path('drivers/edit/<int:id>',views.edit_drivers, name="edit_drivers"),
    path('delete_drivers/<int:id>',views.delete_drivers, name="delete_drivers"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

