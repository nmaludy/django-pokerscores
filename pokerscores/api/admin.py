# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from .models import League, User

admin.site.register(League)
admin.site.register(User)
