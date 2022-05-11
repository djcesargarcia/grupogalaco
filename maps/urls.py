from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [

    path('maps/',views.maps, name="maps"),
    
]
