# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class League(models.Model):
    name = models.TextField()


class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
