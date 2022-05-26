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
    path('', include('driver.urls')),
    path('', include('tmsapp.urls')),
    path('', include('routes.urls')),
    path('', include('login.urls')),
    path('', include('customer.urls')),
    path('', include('article.urls')),
    path('', include('order.urls')),
    path('', include('maps.urls')),
    path('', include('distance.urls')),
    path('', include('provider.urls')),
    path('driver_api/', include('driver_api.urls')),
    path('routes_api/', include('routes_api.urls')),
    path('provider_api/', include('provider_api.urls')),
    path('order_api/', include('order_api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('customer_api/', include('customer_api.urls')),
    path('article_api/', include('article_api.urls')),
    path('loadingplatform_api/', include('loadinplatform_api.urls')),
]
