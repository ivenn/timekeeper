from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'settings', views.SettingsViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tasks', views.TaskViewSet)
