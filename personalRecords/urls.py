from django.conf.urls import patterns, url

from personalRecords import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<record_id>\d+)/$', views.detail, name='detail'),
    url(r'^form/$', views.form, name='form'),
)
