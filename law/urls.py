from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'order.views.index'),
    # url(r'^law/', include('law.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^contacto/$','order.views.contacto'),
)
