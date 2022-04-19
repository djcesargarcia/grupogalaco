from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    
    path('login/',views.login, name="login"),
    path('login/log_in',views.log_in, name="log_in"),
    path('login/log_out',views.log_out, name="log_out"),
    path('login/sign_up',views.sign_up, name="register"),
    path('login/log_error',views.log_error, name="log_error"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
