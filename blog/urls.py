# C:\Users\JACKSON-S-91\dj-django-admin\blog\urls.py
from django.contrib import admin
from django.urls import path, include
I
urlpatterns = [path("admin/", admin.site.urls), path("home", include("blog.urls"))]