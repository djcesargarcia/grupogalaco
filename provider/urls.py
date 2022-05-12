from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('providers/',views.providers, name="providers"),
    path('providers/create',views.create_providers, name="create_providers"),
    path('providers/edit',views.edit_providers, name="edit_providers"),
    path('providers/edit/<int:id>',views.edit_providers, name="edit_providers"),
    path('delete_providers/<int:id>',views.delete_providers, name="delete_providers"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)