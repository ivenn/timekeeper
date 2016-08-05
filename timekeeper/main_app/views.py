from rest_framework import status, mixins, viewsets, authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Settings, Task, Category
from .serializers import UserSerializer, SettingsSerializer, TaskSerializer, CategorySerializer
from .forms import CategoryFilter, TaskFilter


# TODO: replace router's api root with custom one
@api_view(('GET',))
def api_root(request, format=None):
    return Response({ })


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


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD, )


class UserSettingsView(DefaultsMixin,
                       generics.RetrieveAPIView,
                       generics.UpdateAPIView):

    serializer_class = SettingsSerializer

    def get_queryset(self):
        return Settings.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = generics.get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    filter_class = CategoryFilter

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    filter_class = TaskFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
