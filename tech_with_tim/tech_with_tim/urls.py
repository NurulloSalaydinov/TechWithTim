from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('', include('main.urls', namespace="main"))
]
