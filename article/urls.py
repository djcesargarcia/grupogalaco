from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('articles/',views.articles, name="articles"),
    path('articles/create',views.create_articles, name="create_articles"),
    path('articles/edit',views.edit_articles, name="edit_articles"),
    path('articles/edit/<int:id>',views.edit_articles, name="edit_articles"),
    path('articles/<int:id>',views.delete_articles, name="delete_articles"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)