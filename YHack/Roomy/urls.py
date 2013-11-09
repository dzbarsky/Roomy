from django.conf.urls import patterns, url

from Roomy import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^newUser$', views.newUser, name='newUser'),
    url(r'^notes\/$', views.notes, name='notes'),
    url(r'^newHouse$', views.newHouse, name='newHouse'),
    url(r'^createHouse\/$', views.createHouse, name='createHouse'),
    url(r'^charge\/$', views.charge, name='charge'),
    url(r'^doCharge$', views.doCharge, name='doCharge'),
    url(r'^chores\/$', views.chores, name='chores'),
    url(r'^createUser\/$', views.createUser, name='createUser'),
    url(r'^addChore$', views.addChore, name='addChore'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^logout\/$', views.logout, name='logout'),
    url(r'^channel\/*', views.channel, name='channel'),
    url(r'^test\/*', views.test, name='test'),
	url(r'^viewHouse\/$', views.viewHouse, name='viewHouse')
)
