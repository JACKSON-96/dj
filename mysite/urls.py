# C:\Users\JACKSON-S-91\dj-django-admin\mysite\urls.py
from django.urls import path, include, re_path
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
  # Importação correta do módulo admin


urlpatterns = [
    # Redirecionar a URL raiz para a página de admin
    path('', lambda r: HttpResponseRedirect('admin/')),
    path('admin/', admin.site.urls),
    # Aqui você pode incluir as URLs das outras aplicações do seu projeto.
    # path('app/', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()