from django.urls import path
from api_app.views import DriverItemViews

urlpatterns = [
    path('driver-items/', DriverItemViews.as_view())
]