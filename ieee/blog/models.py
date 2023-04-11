from __future__ import annotations
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.query import QuerySet

import uuid


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    thumbnail = models.ImageField(verbose_name="Post Thumbnail", null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)], null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    is_published = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

    @ property
    def get_thumbnail(self):
        """ Returns a thumbnail, or the default thumbnail """
        try:
            url = self.thumbnail.url
        except Exception:
            url = 'uploads/defaultPost.jpg'
        return url

    def get_posts() -> QuerySet[Post]:
        posts = Post.objects.filter(is_published=True)

        if posts.exists():
            return posts
        return None

    def get_post(id: uuid) -> Post:
        post = Post.objects.get(is_published=True, id=id)

        if post:
            return post

        return None
