from django.conf.urls import patterns, url

from Roomy import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^newUser$', views.newUser, name='newUser'),
    url(r'^notes\/$', views.notes, name='notes'),
    url(r'^savedNotes$', views.savedNotes, name='savedNotes'),
    url(r'^newHouse$', views.newHouse, name='newHouse'),
    url(r'^createHouse\/$', views.createHouse, name='createHouse'),
    url(r'^charge\/$', views.charge, name='charge'),
    url(r'^doCharge$', views.doCharge, name='doCharge'),
    url(r'^chores\/$', views.chores, name='chores'),
    url(r'^createUser\/$', views.createUser, name='createUser'),
    url(r'^addChore$', views.addChore, name='addChore'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^logout\/$', views.logout, name='logout'),
    url(r'^viewHouse\/$', views.viewHouse, name='viewHouse'),
    url(r'^textReminder\/$', views.textReminder, name='textReminder'),
    url(r'^.*', views.view404, name='404'),
)
