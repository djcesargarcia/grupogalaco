from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
   
    path('customers/index.html',views.customers, name="customers"),
    path('customers/create',views.create_customers, name="create_customers"),
    path('customers/edit',views.edit_customers, name="edit_customers"),  
    path('customers/edit/<int:id>',views.edit_customers, name="edit_customers"),
    path('delete_customers/<int:id>',views.delete_customers, name="delete_customers"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)