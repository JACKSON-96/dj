# C:\Users\JACKSON-S-91\dj-django-admin\blog\admin.py

from django.contrib import admin
from .models import Post  # Certifique-se de que Post é o nome correto do seu modelo

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}  # Note que a chave do dicionário é 'slug', não 'slug:'

admin.site.register(Post, PostAdmin)  # Aqui, Post e PostAdmin não devem estar entre aspas
