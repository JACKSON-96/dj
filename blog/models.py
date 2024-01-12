# C:\Users\JACKSON-S-91\dj-django-admin\blog\models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    status = models.CharField(max_length=10)
    created_on = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title