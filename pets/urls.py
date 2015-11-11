from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^add-pet/$', views.add_pet, name='add-pet'),

	url(r'^(?P<pk>[0-9]+)/$', views.get_pet, name='pet'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_detail, name='edit-detail'),

	url(r'^(?P<pk>[0-9]+)/tasks/$', views.get_tasks, name='tasks'),
	url(r'^tasks/new/$', views.add_task, name='add-task'),
	url(r'^tasks/(?P<pk>[0-9]+)/edit/$', views.edit_task, name='edit-task'),
]