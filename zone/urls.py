from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('zones/',views.zones, name="zones"),
    path('zones/create',views.create_zones, name="create_zones"),
    path('zones/edit',views.edit_zones, name="edit_zones"),
    path('zones/edit/<int:id>',views.edit_zones, name="edit_zones"),
    path('zones/<int:id>',views.delete_zones, name="delete_zones"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)