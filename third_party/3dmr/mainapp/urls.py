from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^docs$', views.docs, name='docs'),
    url(r'^downloads$', views.downloads, name='downloads'),
    url(r'^model/(?P<model_id>[0-9]+)$', views.model, name='model'),
    url(r'^model/(?P<model_id>[0-9]+)/(?P<revision>[0-9]+)$', views.model, name='model'),
    url(r'^search$', views.search, name='search'),
    url(r'^search$', views.search, name='search'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^revise/(?P<model_id>[0-9]+)$', views.revise, name='revise'),
    url(r'^edit/(?P<model_id>[0-9]+)/(?P<revision>[0-9]+)$', views.edit, name='edit'),
    url(r'^user/(?P<username>.*)$', views.user, name='user'),
    url(r'^map$', views.modelmap, name='map'),
    url(r'^action/editprofile$', views.editprofile, name='editprofile'),
    url(r'^action/addcomment$', views.addcomment, name='addcomment'),
    url(r'^action/ban$', views.ban, name='ban'),
    url(r'^action/hide_model$', views.hide_model, name='hide_model'),
    url(r'^action/hide_comment$', views.hide_comment, name='hide_comment'),
    url(r'^action/new_token$', views.new_token, name='new_token'),

    url(r'^api/info/(?P<model_id>[0-9]+)$', api.get_info, name='get_info'),

    url(r'^api/model/(?P<model_id>[0-9]+)/(?P<revision>[0-9]+)$', api.get_model, name='get_model'),
    url(r'^api/model/(?P<model_id>[0-9]+)$', api.get_model, name='get_model'),
    url(r'^api/filelist/(?P<model_id>[0-9]+)/(?P<revision>[0-9]+)$', api.get_filelist, name='get_list'),
    url(r'^api/filelist/(?P<model_id>[0-9]+)$', api.get_filelist, name='get_list'),
    url(r'^api/file/(?P<model_id>[0-9]+)/(?P<revision>[0-9]+)/(?P<filename>.+)$', api.get_file, name='get_file'),
    url(r'^api/filelatest/(?P<model_id>[0-9]+)/(?P<filename>.+)$', api.get_file, name='get_file'),

    url(r'^api/tag/(?P<tag>.*)/(?P<page_id>[0-9]+)$', api.lookup_tag, name='lookup_tag'),
    url(r'^api/tag/(?P<tag>.*)$', api.lookup_tag, name='lookup_tag'),
    url(r'^api/category/(?P<category>.*)/(?P<page_id>[0-9]+)$', api.lookup_category, name='lookup_category'),
    url(r'^api/category/(?P<category>.*)$', api.lookup_category, name='lookup_category'),
    url(r'^api/author/(?P<username>.*)/(?P<page_id>[0-9]+)$', api.lookup_author, name='lookup_author'),
    url(r'^api/author/(?P<username>.*)$', api.lookup_author, name='lookup_author'),

    url(r'^api/search/?(?P<latitude>-?[0-9]+(\.[0-9]+)?)/(?P<longitude>-?[0-9]+(\.[0-9]+)?)/(?P<distance>[0-9]+(\.[0-9]+)?)/(?P<page_id>[0-9]+)$', api.search_range, name='lookup_range'),
    url(r'^api/search/(?P<latitude>-?[0-9]+(\.[0-9]+)?)/(?P<longitude>-?[0-9]+(\.[0-9]+)?)/(?P<distance>[0-9]+(\.[0-9]+)?)$', api.search_range, name='lookup_range'),
    url(r'^api/search/title/(?P<title>.*)/(?P<page_id>[0-9]+)$', api.search_title, name='search_title'),
    url(r'^api/search/title/(?P<title>.*)$', api.search_title, name='search_title'),
    url(r'^api/search/full$', api.search_full, name='search_full'),
]
