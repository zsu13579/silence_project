"""silence_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^silence/', 'silence.views.testuserlist'),
    url(r'^login', 'silence.views.do_login'),
    url(r'^$', 'silence.views.do_login'),
    url(r'^searchresult/', 'silence.views.searchresult'),
    url(r'^callsearchresult/', 'silence.views.callsearchresult'),
    url(r'^savecall/', 'silence.views.savecall'),
    url(r'^calldetail/', 'silence.views.calldetail'),
    url(r'^dashboard/', 'silence.views.dashboard'),
    url(r'^promotion/', 'silence.views.promotion'),
]
