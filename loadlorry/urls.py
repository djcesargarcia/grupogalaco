from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros',views.nosotros, name="nosotros"),
    path('loadlorries/',views.loadlorries, name="loadlorries"),
    path('loadlorries/create',views.create_loadlorries, name="create_loadlorries"),
    path('loadlorries/edit',views.edit_loadlorries, name="edit_loadlorries"),
    path('loadlorries/edit/<int:id>',views.edit_loadlorries, name="edit_loadlorries"),
    path('delete_loadlorries/<int:id>',views.delete_loadlorries, name="delete_loadlorries"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

