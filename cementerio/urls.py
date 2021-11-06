# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Inicio.as_view(), name='inicio'),
    url(r'^clientes/$', views.Clientes.as_view(), name='clientes'),
    url(r'^clientes/agregar/$', views.ClientesAgregar.as_view(), name='clientesagregar'),
    url(r'^clientes/(?P<pk>[0-9]+)/$', views.ClientesDetalle.as_view(), name='clientesdetalle'),
    url(r'^clientes/modificar/(?P<pk>[0-9]+)/$', views.ClientesModificar.as_view(), name='clientesmodificar'),
    url(r'^clientes/(?P<pk>[0-9]+)/agregar/terreno/$', views.ClientesAgregarTerreno.as_view(), name='clientesagregarterreno'),
    url(r'^clientes/eliminar/(?P<pk>[0-9]+)/$', views.ClientesEliminar.as_view(), name='clienteseliminar'),
    url(r'^terrenos/$', views.Terrenos.as_view(), name='terrenos'),
    url(r'^terrenos/(?P<pk>[0-9]+)/$', views.TerrenosDetalle.as_view(), name='terrenosdetalle'),
    url(r'^terrenos/modificar/(?P<pk>[0-9]+)/$', views.TerrenosModificar.as_view(), name='terrenosmodificar'),
    url(r'^terrenos/eliminar/(?P<pk>[0-9]+)/$', views.TerrenosEliminar.as_view(), name='terrenoseliminar'),
    url(r'^terrenos/(?P<pk>[0-9]+)/agregar/difunto/$', views.TerrenosAgregarDifunto.as_view(), name='terrenosagregardifunto'),
    url(r'^terrenos/(?P<pk>[0-9]+)/recibodepago/$', views.TerrenosRecibo.as_view(), name='terrenosrecibo'),
    url(r'^difuntos/$', views.Difuntos.as_view(), name='difuntos'),
    url(r'^difuntos/(?P<pk>[0-9]+)/$', views.DifuntosDetalle.as_view(), name='difuntosdetalle'),
    url(r'^difuntos/modificar/(?P<pk>[0-9]+)/$', views.DifuntosModificar.as_view(), name='difuntosmodificar'),
    url(r'^difuntos/eliminar/(?P<pk>[0-9]+)/$', views.DifuntosEliminar.as_view(), name='difuntoseliminar'),
]
