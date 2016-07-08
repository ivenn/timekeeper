from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^personal/$', views.user_personal, name='personal'),
    url(r'^settings/$', views.user_settings, name='settings'),
    url(r'^reports/$', views.user_reports, name='reports'),
    url(r'^registration/$', views.user_registration, name='registration'),

    url(r'^$', views.index, name='index'),
]
