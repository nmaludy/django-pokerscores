# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class League(models.Model):
    name = models.TextField()


# Note: this is really a "user", but since Django already provides a User
#       model we don't want to override it. Instead we want to create some
#       additional properties and link it to a user.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leagues = models.ManyToManyField(League)


# automatically create/update profile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
