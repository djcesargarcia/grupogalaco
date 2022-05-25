from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('loadingplatforms/',views.areas, name="areas"),
    path('loadingplatforms/create',views.create_areas, name="create_areas"),
    path('loadingplatforms/edit',views.edit_areas, name="edit_areas"),
    path('loadingplatforms/edit/<int:id>',views.edit_areas, name="edit_areas"),
    path('loadingplatforms/<int:id>',views.delete_areas, name="delete_areas"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)