from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'projects/', views.projects, name='projects'),
    re_path(r'^project/(?P<project_id>\d+)/$', views.project, name = 'project'),
    re_path(r'^new_project/$', views.new_project, name = 'new_project'),
    re_path(r'^new_opinion/(?P<project_id>\d+)/$', views.new_opinion, name='new_opinion'),
    re_path(r'^edit_opinion/(?P<opinion_id>\d+)/$', views.edit_opinion, name='edit_opinion'),
    re_path(r'^delete_project/(?P<project_id>\d+)/$', views.delete_project, name='delete_project'),
    re_path(r'^delete_opinion/(?P<opinion_id>\d+)/$', views.delete_opinion, name='delete_opinion'),
    re_path(r'^search_project/', views.search, name='search')
]