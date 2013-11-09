from django.conf.urls import patterns, url

from Roomy import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^newUser$', views.newUser, name='newUser'),

)
