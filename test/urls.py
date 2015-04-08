from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test.views.home', name='home'),
    url(r'^', include('location.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'test.views.home', name='home'),
)
