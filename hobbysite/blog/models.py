from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    