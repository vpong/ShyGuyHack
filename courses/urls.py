from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^(?P<course_id>\d+)/$', views.details, name='details'),
)
