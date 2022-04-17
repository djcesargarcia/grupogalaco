from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    
    path('tmsapp/',views.tmsapp, name="tmsapp"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)