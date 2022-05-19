from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('provider/',views.provider, name="provider"),
    path('provider/create',views.create_provider, name="create_provider"),
    path('provider/edit',views.edit_provider, name="edit_provider"),
    path('provider/edit/<int:id>',views.edit_provider, name="edit_provider"),
    path('delete_provider/<int:id>',views.delete_provider, name="delete_provider"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)