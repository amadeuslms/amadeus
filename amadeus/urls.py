from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Eu adicionei:
#from  django.conf.urls.defaults import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    #Eu adicionei:
    url(r'^$', 'core.views.user'),
    url(r'^cadastro/', include('core.urls', namespace='core')),
    #url(r'^cadastro/', include('users.urls')),

    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

#quando estiver num ambiente de producao, retirar este bloco:
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )