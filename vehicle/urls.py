from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    
    path('vehicles/', views.vehicles , name="vehicles"),
    path('vehicles/create', views.create_vehicles , name="create_vehicles"),
    path('vehicles/edit', views.edit_vehicles , name="edit_vehicles"),
    path('vehicles/edit/<int:id>',views.edit_vehicles, name="edit_vehicles"),
    path('delete_vehicles/<int:id>',views.delete_vehicles, name="delete_vehicles"),
      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

