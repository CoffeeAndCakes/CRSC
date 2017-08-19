from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^genres/(?P<genre_id>[0-9]+)/$', views.genres_result, name='genres'),
    url(r'^years/(?P<year>[0-9]+)/$', views.years_result, name='years'),
]
