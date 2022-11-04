# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.Inicio.as_view(), name='inicio'),
    re_path(r'^clientes/$', views.Clientes.as_view(), name='clientes'),
    re_path(r'^clientes/agregar/$', views.ClientesAgregar.as_view(),
            name='clientesagregar'),
    re_path(r'^clientes/(?P<pk>[0-9]+)/$',
            views.ClientesDetalle.as_view(), name='clientesdetalle'),
    re_path(r'^clientes/modificar/(?P<pk>[0-9]+)/$',
            views.ClientesModificar.as_view(), name='clientesmodificar'),
    re_path(r'^clientes/(?P<pk>[0-9]+)/agregar/terreno/$',
            views.ClientesAgregarTerreno.as_view(), name='clientesagregarterreno'),
    re_path(r'^clientes/eliminar/(?P<pk>[0-9]+)/$',
            views.ClientesEliminar.as_view(), name='clienteseliminar'),
    re_path(r'^terrenos/$', views.Terrenos.as_view(), name='terrenos'),
    re_path(r'^terrenos/(?P<pk>[0-9]+)/$',
            views.TerrenosDetalle.as_view(), name='terrenosdetalle'),
    re_path(r'^terrenos/modificar/(?P<pk>[0-9]+)/$',
            views.TerrenosModificar.as_view(), name='terrenosmodificar'),
    re_path(r'^terrenos/eliminar/(?P<pk>[0-9]+)/$',
            views.TerrenosEliminar.as_view(), name='terrenoseliminar'),
    re_path(r'^terrenos/(?P<pk>[0-9]+)/agregar/difunto/$',
            views.TerrenosAgregarDifunto.as_view(), name='terrenosagregardifunto'),
    re_path(r'^terrenos/(?P<pk>[0-9]+)/recibodepago/$',
            views.TerrenosRecibo.as_view(), name='terrenosrecibo'),
    re_path(r'^difuntos/$', views.Difuntos.as_view(), name='difuntos'),
    re_path(r'^difuntos/(?P<pk>[0-9]+)/$',
            views.DifuntosDetalle.as_view(), name='difuntosdetalle'),
    re_path(r'^difuntos/modificar/(?P<pk>[0-9]+)/$',
            views.DifuntosModificar.as_view(), name='difuntosmodificar'),
    re_path(r'^difuntos/eliminar/(?P<pk>[0-9]+)/$',
            views.DifuntosEliminar.as_view(), name='difuntoseliminar'),
]
