from django.conf.urls import patterns, include, url

from articles.views import HelloTemplate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^join/$', 'accounts.views.join', name='join'),
    #url(r'^auth/$', 'accounts.views.auth_view', name='auth'),
    
    #url(r'^logout/$', 'accounts.views.logout'),
    #url(r'^loggedin/$', 'accounts.views.loggedin'),
    #url(r'^invalid/$', 'accounts.views.invalid_login'),
)
