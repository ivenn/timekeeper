from rest_framework import viewsets, authentication, permissions

from .models import User, Settings, Task, Category
from .serializers import UserSerializer, SettingsSerializer, TaskSerializer, CategorySerializer


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD, )


class SettingsViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
