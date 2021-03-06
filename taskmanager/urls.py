from django.conf.urls import patterns, include, url
from taskmanager import views


urlpatterns = patterns('',

    url(r'^$', views.cities, name="participant-register"), 
    url(r'^cities/(?P<id>\d+)/persons/$', views.personlist, name="persons_list"),
    url(r'^tests_by_month/$', views.persons_by_month, name="persons_by_month_list"),
    url(r'^tests_by_week/$', views.persons_by_week, name="persons_by_week_list"),
    url(r'^tests_by_day/$', views.persons_by_day, name="persons_by_day_list"),
    url(r'^person/(?P<id>\d+)/$', views.person_details, name="person_detail"),

)
