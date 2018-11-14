# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http import HttpResponse

from .models import League


def index(request):
    return HttpResponse("Hello, world. You're at the API index.")


def leagues_list(request):
    leagues = League.objects.order_by('-id')
    output = serializers.serialize("json", leagues)
    return HttpResponse(output)
    # return HttpResponse("You're looking at all leagues.")


def leagues_get(request, league_id):
    return HttpResponse("You're looking at league %s." % league_id)


def leagues_users_list(request, league_id):
    return HttpResponse("You're looking at league %s, all users." % league_id)


def leagues_users_get(request, league_id, user_id):
    return HttpResponse("You're looking at league %s, user %s." % (league_id, user_id))
