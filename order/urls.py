from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('orders/',views.orders, name="orders"),
    path('orders/create',views.create_orders, name="create_orders"),
    path('orders/edit',views.edit_orders, name="edit_orders"),
    path('orders/edit/<int:id>',views.edit_orders, name="edit_orders"),
    path('delete_orders/<int:id>',views.delete_orders, name="delete_orders"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)