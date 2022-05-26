from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
   
    path('docks/index.html',views.docks, name="docks"),
    path('docks/create',views.create_docks, name="create_docks"),
    path('docks/edit',views.edit_docks, name="edit_docks"),  
    path('docks/edit/<int:id>',views.edit_docks, name="edit_docks"),
    path('delete_docks/<int:id>',views.delete_docks, name="delete_docks"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)