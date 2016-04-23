from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^$', views.main_page, name='main_page'),
    url(r'^requests$', views.requests10, name='requests10'),
    url(r'^requests10$', views.requests10, name='requests10'),
    url(r'^chknewreq$', views.chknewreq, name='chknewreq'),
)
