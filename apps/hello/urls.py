from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^$', views.main_page, name='main_page'),
    url(r'^index.html$', views.main_page, name='main_page'),
    url(r'^requests_page$', views.requests_page, name='requests_page'),
    url(r'^chknewreq$', views.chknewreq, name='chknewreq'),
    url(r'^editor_page$', views.editor_page, name='editor_page'),
)
