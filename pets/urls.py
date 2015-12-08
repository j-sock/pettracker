from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.log_in, name='login'),
	url(r'^logout/$', views.log_out, name='logout'),

	url(r'^humans/(?P<pk>[0-9]+)/$', views.get_human, name='human'),

	url(r'^pets/(?P<pk>[0-9]+)/$', views.get_pet, name='pet'),
	url(r'^add-pet/$', views.add_pet, name='add-pet'),
	url(r'^pets/(?P<pk>[0-9]+)/edit/$', views.edit_detail, name='edit-detail'),

	url(r'^tasks/$', views.get_tasks, name='tasks'),
	url(r'^tasks/new/$', views.add_task, name='add-task'),
	url(r'^tasks/(?P<pk>[0-9]+)/edit/$', views.edit_task, name='edit-task'),
	url(r'^tasks/(?P<pk>[0-9]+)/check/$', views.do_task, name='do-task'),
]