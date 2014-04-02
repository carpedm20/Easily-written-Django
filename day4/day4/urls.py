from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^articles/', include('articles.urls', namespace='articles')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^admin/', include(admin.site.urls), name='admin'),
)
