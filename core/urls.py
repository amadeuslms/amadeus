from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^$', 'user', name='user'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)