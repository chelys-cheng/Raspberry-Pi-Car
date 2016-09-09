from django.conf.urls import patterns, url
from control_car import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^(?P<act>[0-9]+)/$', views.Car_act, name="a"),
)
