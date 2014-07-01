from django.conf.urls import patterns, url

from find_dj import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index')
)
	url(r'^(?P<dj_id>\d+)/$', views.dj_view, name='dj_view')
)