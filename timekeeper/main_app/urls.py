from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.conf.urls import url, include


from . import views


router = DefaultRouter()

# admin
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'tasks', views.TaskViewSet, base_name='tasks')

