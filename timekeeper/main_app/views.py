from rest_framework import viewsets, authentication, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .models import User, Settings, Task, Category
from .serializers import UserSerializer, SettingsSerializer, TaskSerializer, CategorySerializer
from .forms import SettingsFilter, CategoryFilter, TaskFilter


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


class AdminMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD, )

    """
    @detail_route(url_path='settings')
    def get_settings(self, request, username=None):
        user = self.get_object()
        settings = Settings.objects.get(user=user)
        sserializer = SettingsSerializer(settings)
        return Response(sserializer.data)
    """

class SettingsViewSet(DefaultsMixin, viewsets.ModelViewSet):

    serializer_class = SettingsSerializer
    filter_class = SettingsFilter

    def get_queryset(self):
        return Settings.objects.filter(user=self.request.user)


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    filter_class = CategoryFilter

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):

    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    serializer_class = TaskSerializer
    filter_class = TaskFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
