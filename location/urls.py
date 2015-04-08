from django.conf.urls import patterns, include, url

urlpatterns = patterns('location.views',
	url(r'^app/route/$','route', name='route'),
)
