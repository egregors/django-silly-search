# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    text = models.TextField()


class News(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()


class Item(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
