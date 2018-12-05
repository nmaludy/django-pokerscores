# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer, LeagueSerializer, ProfileSerializer
from .models import League, Profile


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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leagues to be viewed or edited.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
