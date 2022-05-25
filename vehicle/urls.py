from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    
    path('vehicles/', views.routes , name="routes"),
    path('vehicles/create', views.create_routes , name="create_routes"),
    path('vehicles/edit', views.edit_routes , name="edit_routes"),
    path('vehicles/edit/<int:id>',views.edit_routes, name="edit_routes"),
    path('delete_vehicles/<int:id>',views.delete_routes, name="delete_routes"),
      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

