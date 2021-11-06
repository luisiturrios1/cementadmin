# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView

from cementerio.models import Cliente


class ClientesModificar(PermissionRequiredMixin, UpdateView):

    permission_required = 'cementerio.change_cliente'

    model = Cliente

    fields = [
        'nombre',
        'apellido',
        'telefono',
        'direccion',
        'notas',
        'beneficiario_1',
        'beneficiario_2',
    ]

    template_name = 'cementerio/clientes/clientesmodificar.html'
