from django.conf.urls import patterns, include, url

import os
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^webtoon/$', 'webtoon.views.home', name='webootn'),
	url(r'^webtoon/author/(?P<author_id>\d+)/$', 'webtoon.views.author', name='author'),
	url(r'^webtoon/(?P<comic_id>\d+)/$', 'webtoon.views.comic', name='comic'),
	url(r'^webtoon/(?P<comic_id>\d+)/(?P<episode_id>\d+)/$', 'webtoon.views.episode', name='episode'),

	('^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root':
		 os.path.join(os.path.dirname(__file__),'media')}
	),

    url(r'^admin/', include(admin.site.urls)),
)
