import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    frequency = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    status = models.IntegerField()
    created = models.DateTimeField('Date Created')
    published = models.DateTimeField('Date Published')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField('Date Created')
    email = models.EmailField()
    url = models.URLField()
