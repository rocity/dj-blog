import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    HIDDEN = 'hidden'
    DELETED = 'deleted'
    STATUSES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (HIDDEN, 'Hidden'),
        (DELETED, 'Deleted'),
        )
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=50,
                                choices=STATUSES,
                                default=DRAFT)
    created = models.DateTimeField('Date Created',
                                    auto_now_add=True,
                                    blank=True)
    published = models.DateTimeField('Date Published',
                                        auto_now=True)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title

    def get_post_comments(self):
        return Comment.objects.filter(
            status__exact='published',
            post__id__exact=self.pk
        ).order_by('-created')[:5]

class Comment(models.Model):
    PUBLISHED = 'published'
    HIDDEN = 'hidden'
    DELETED = 'deleted'
    STATUSES = (
        (PUBLISHED, 'Published'),
        (HIDDEN, 'Hidden'),
        (DELETED, 'Deleted'),
        )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=50,
                                choices=STATUSES,
                                default=HIDDEN)
    created = models.DateTimeField('Date Created',
                                        auto_now_add=True,
                                        blank=True)
    name = models.CharField(blank=False,
                            null=False,
                            max_length=50,
                            default='Anonymous')
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.content
