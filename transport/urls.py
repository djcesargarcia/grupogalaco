from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('drivers', views.drivers, name='drivers'),
    path('drivers', views.create, name='create'),
    path('drivers', views.edit, name='edit'),
    path('home', views.home, name='home'),
    path('routes', views.routes, name="routes"),
    path('routes', views.create, name="create"),
    path('routes', views.edit, name="edit"),
    path('customers', views.customers, name="customers"),
    path('warehouses', views.warehouses, name="warehouses")
]


