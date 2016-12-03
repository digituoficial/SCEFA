from django.conf.urls import url
from appPonto.views import *

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^funcionario/list$',funcionario_list,name='funcionario_list'),
    url(r'^funcionario/detail/(?P<pk>\d+)$',funcionario_detail,name='funcionario_detail'),
    url(r'^funcionario/new/$',funcionario_new,name='funcionario_new'),
    url(r'^funcionario/update/(?P<pk>\d+)$',funcionairo_update,name='funcionario_update'),
    url(r'^funcionario/delete/(?P<pk>\d+)$', funcionario_delete, name='funcionario_delete'),

    url(r'^administrador/list$',administrador_list,name='administrador_list'),
    url(r'^administrador/detail/(?P<pk>\d+)$',administrador_detalhe,name='administrador_detail'),
    url(r'^administrador/new/$',administrador_new,name='funcionario_new'),
    url(r'^administrador/update/(?P<pk>\d+)$',administrador_update,name='administrador_update'),
    url(r'^administrador/delete/(?P<pk>\d+)$', administrador_delete, name='administrador_delete'),
]