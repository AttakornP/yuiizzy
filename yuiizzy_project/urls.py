from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yuiizzy.views.home', name='home'),
    # url(r'^yuiizzy/', include('yuiizzy.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
