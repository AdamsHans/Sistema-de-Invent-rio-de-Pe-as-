from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # path('admin/', admin.site.urls), para acessar com http://127.0.0.1:8000//admin
    path('', admin.site.urls), # para acessar sem http://127.0.0.1:8000/
]
