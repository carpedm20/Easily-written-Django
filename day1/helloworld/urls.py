from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^me/([\w]+)/([\w]+)/([\w]+)/', 'helloworld.views.me'),
    url(r'^$', 'helloworld.views.hello'), 
    url(r'^([\w]+)/', 'helloworld.views.hello'), 
)
