# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models


class Article(models.Model):
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
    price = models.DecimalField(max_digits=6, decimal_places=2)
