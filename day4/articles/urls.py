from django.conf.urls import patterns, include, url

from articles.views import HelloTemplate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'articles.views.articles'),
    url(r'^all/$', 'articles.views.articles', name='all'),
    url(r'^get/(?P<article_id>\d+)/$', 'articles.views.article', name='get'),

    url(r'^language/(?P<language>[a-z\-]+)/$', 'articles.views.language', name='language'),

    url(r'^hello/', 'articles.views.hello'),
    url(r'^hello_class/', HelloTemplate.as_view()),
)
