from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('areas/',views.areas, name="areas"),
    path('areas/create',views.create_areas, name="create_areas"),
    path('areas/edit',views.edit_areas, name="edit_areas"),
    path('areas/edit/<int:id>',views.edit_areas, name="edit_areas"),
    path('areas/<int:id>',views.delete_areas, name="delete_areas"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)