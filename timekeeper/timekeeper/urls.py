
from django.conf.urls import include, url

from rest_framework.authtoken.views import obtain_auth_token
from main_app import views

from main_app.urls import router


urlpatterns = [
    url(r'^api/token/$', obtain_auth_token, name='api-token'),
    url(r'^api/settings/$', views.UserSettingsView.as_view(), name='user-settings'),
    url(r'^api/', include(router.urls)),
]
