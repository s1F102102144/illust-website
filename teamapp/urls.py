from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('preview/<int:image_id>/', views.preview, name='preview'),
    path('upload/', views.upload, name="upload"),
    path('api/articles/<int:article_id>/like', views.api_like, name="api_like"),
]