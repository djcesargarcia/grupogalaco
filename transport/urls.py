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
    path('customers', views.create, name="create"),
    path('customers', views.edit, name="edit"),
    path('warehouses', views.warehouses, name="warehouses"),
    path('warehouses', views.create, name="create"),
    path('warehouses', views.edit, name="edit"),
    path('users', views.users, name="users"),
    path('users', views.create, name="create"),
    path('users', views.edit, name="edit")
]


