from django.conf.urls import patterns, include, url

from articles.views import HelloTemplate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^all/$', 'articles.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'articles.views.article'),
    url(r'^hello/', 'articles.views.hello'),
    url(r'^hello_class/', HelloTemplate.as_view()),
)
