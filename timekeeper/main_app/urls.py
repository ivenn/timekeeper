from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

# admin
router.register(r'users', views.UserViewSet)
router.register(r'category', views.CategoryViewSet, base_name='categories')
router.register(r'tasks', views.TaskViewSet, base_name='tasks')

