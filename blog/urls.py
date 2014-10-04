__author__ = 'ntech'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from blog.views import *

urlpatterns = patterns('',
    url(r'^login/', TemplateView.as_view(template_name="login.html")),
    # url(r'^login/$', Loginview.as_view),
    url(r'^signup', Signup_view.as_view(), name='signup'),
    # url(r'^signup/$', Signup_view.as_view, name='signup'),
    url(r'^welcome/$', TemplateView.as_view(template_name="welcome.html")),
)