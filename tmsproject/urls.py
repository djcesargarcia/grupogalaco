from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transport.urls')),
    path('login/', include('login.urls')),
    path('login/', include('django.contrib.auth.urls'))
]
