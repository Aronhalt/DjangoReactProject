from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^api/(?P<pk>[0-9]+)/$', views.projectDetail.as_view(), name='projectDetail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
