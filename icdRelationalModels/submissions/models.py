from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    pass

class Author(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField(Article)