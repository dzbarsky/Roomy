from django.conf.urls import patterns, url

from Roomy import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^newUser$', views.newUser, name='newUser'),
    url(r'^lists\/$', views.lists, name='lists'),
    url(r'^newHouse$', views.newHouse, name='newHouse'),
    url(r'^createHouse\/$', views.createHouse, name='createHouse'),
    url(r'^charge\/$', views.charge, name='charge'),
    url(r'^chores\/$', views.chores, name='chores'),
)
