from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import HelloTemplate
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^all/$' , 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$' , 'article.views.article'),
	url(r'^language/(?P<language>[a-z\-]+)/$' , 'article.views.language'),
	url(r'^create/$' , 'article.views.create'),
	url(r'^search/$' , 'article.views.search_titles'),
)


