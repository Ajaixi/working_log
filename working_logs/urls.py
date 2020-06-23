from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'projects/(?P<pindex>\d*)/$', views.projects, name='projects'),
    re_path(r'results/(?P<projects_name>\w*)/(?P<pindex>\d+)/$', views.results, name='results'),
    re_path(r'^project/(?P<project_id>\d+)/$', views.project, name ='project'),
    re_path(r'^review/(?P<project_id>\d+)/$', views.review, name ='review'),
    re_path(r'^new_project/$', views.new_project, name = 'new_project'),
    re_path(r'^new_opinion/(?P<project_id>\d+)/$', views.new_opinion, name='new_opinion'),
    re_path(r'^edit_opinion/(?P<opinion_id>\d+)/$', views.edit_opinion, name='edit_opinion'),
    re_path(r'^delete_project/(?P<project_id>\d+)/$', views.delete_project, name='delete_project'),
    re_path(r'^delete_opinion/(?P<opinion_id>\d+)/$', views.delete_opinion, name='delete_opinion'),
    re_path(r'^search_project/', views.search, name='search'),
    re_path(r'^add_img/(?P<project_id>\d+)/$', views.img_upload, name='add_img'),
    re_path(r'^show_img/(?P<project_id>\d+)/$', views.img_show, name='show_img'),
    re_path(r'^delete_img/(?P<img_id>\d+)/$', views.delete_img, name='delete_img'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)