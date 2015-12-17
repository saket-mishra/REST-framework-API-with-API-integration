from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from patients import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^cities/$',
        views.CityList.as_view(),
        name='city-list'),
     url(r'^cities/(?P<pk>[0-9]+)/persons/$',
        views.CityDetail.as_view(),
        name='city-detail'),
    url(r'^person/(?P<pk>[0-9]+)/$',
        views.PersonDetail.as_view(),
        name='person-detail'),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
