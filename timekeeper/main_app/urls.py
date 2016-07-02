from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^main/$', views.user_main, name='main'),
    url(r'^settings/$', views.user_settings, name='settings'),
    url(r'^reports/$', views.user_reports, name='reports'),
]
