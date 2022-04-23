
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .index_view import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('api.urls')),
    path('', obtain_auth_token)
]