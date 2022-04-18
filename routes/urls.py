from django.urls import path, include
from . import views

urlpatterns = [
    
    path('routes/', views.routes , name="routes"),
    path('routes/create', views.create_routes , name="create_routes"),
    path('routes/edit', views.edit_routes , name="edit_routes"),
    path('routes/edit/<int:id>',views.edit_routes, name="edit_routes"),
    path('delete_routes/<int:id>',views.delete_routes, name="delete_routes"),
    
]