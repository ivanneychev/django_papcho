from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)


class Friend(models.Model):
    users = models.ManyToManyField(User)
