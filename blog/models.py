from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=400)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/', null=True)
