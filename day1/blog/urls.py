from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^helloworld/', 'helloworld.views.index'),
    url(r'^helloworld/', include('helloworld.urls')),
    url(r'^post/', include('post.urls')),

    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
