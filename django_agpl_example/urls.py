from django.conf.urls.defaults import *

urlpatterns = patterns('',
   url(r'^$', 'example.views.index', name='index'),
   (r'^download/', include('django_agpl.urls')),
)
