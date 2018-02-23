from django.conf.urls import patterns, url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.loginapp, name="loginapp"),
    url(r'^logout/$', views.logoutapp, name="logoutapp"),
    url(r'^round1/$', views.round1, name="round1"),
    url(r'^round2/$', views.round2, name="round2"),
    url(r'^round2upload/$', views.round2upload, name="round2upload"),
    url(r'^scorecard/$', views.scorecard, name ="scorecard"),
    url(r'^adminmanage/$', views.adminmanage, name="adminmanage"),
    url(r'^endround2/$', views.endround2, name="endround2"),
	url(r'^ascii/$', views.ascii, name="ascii"),
 ]