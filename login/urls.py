from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    
    path('login/',views.login, name="login"),
    path('login/signin',views.login_signin, name="login_signin"),
    path('login/signout',views.login_signout, name="login_signout"),
    path('login/signup',views.login_signout, name="login_signup"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
