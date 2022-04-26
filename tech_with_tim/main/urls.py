from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('teachers/', views.teachers, name='teachers'),
]
