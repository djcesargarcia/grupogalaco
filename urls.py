"""tmsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drivers.urls')),
    path('', include('tmsapp.urls')),
    path('', include('login.urls')),
    path('', include('articles.urls')),
    path('', include('maps.urls')),
    path('', include('distance.urls')),
    path('', include('provider.urls')),
    path('', include('area.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('driver_api.urls')),
    path('',include('routes_api.urls')),
    path('',include('order_api.urls')),
    path('',include('customer_api.urls')),
    path('', include('article_api.urls')),
    path('', include('zone_api.urls')),
    path('', include('vehicle_api.urls')),
]
