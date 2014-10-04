__author__ = 'ntech'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from blog.views import *

urlpatterns = patterns('',
    url(r'^login/', Loginview.as_view(), name='Login'),
    url(r'^signup', Signup_view.as_view(), name='signup'),
    url(r'^logout/', Logout_view.as_view(), name='Logout'),
    url(r'^welcome/$', TemplateView.as_view(template_name="welcome.html")),
)