from django.conf.urls import patterns, url

from find_dj import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index')
)