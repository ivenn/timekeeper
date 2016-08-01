from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.conf.urls import url, include


from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)