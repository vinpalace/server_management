from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    # url(r'^(?P<product_id>[0-9]+)$', detail, name="detail"),
    url(r'^(?P<pk>\d+)$', detail, name="detail"),
    url(r'^edit/(?P<pk>\d+)$', edit, name="edit"),
    url(r'^addnew$', addnew, name="addnew"),
    url(r'^addnew_linux$', addnew_linux, name="addnew_linux"),
    url(r'^addnew_windows$', addnew_windows, name="addnew_windows"),
    url(r'^addnew_network$', addnew_network, name="addnew_network"),
    url(r'^windows$', windows, name="windows"),
    url(r'^linux$', linux, name="linux"),
    url(r'^network$', network, name="network"),
    url(r'^delete/(?P<pk>\d+)/(?P<header>[\w\-]+)/$', delete, name="delete"),

]
