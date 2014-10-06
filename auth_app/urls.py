__author__ = 'ntech'

from django.conf.urls import patterns, include, url
from auth_app import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    )
