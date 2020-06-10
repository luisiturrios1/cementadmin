# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView

from cementerio.models import Difunto


class DifuntosModificar(PermissionRequiredMixin, UpdateView):

    permission_required = 'cementerio.change_difunto'

    model = Difunto

    fields = ['nombre', 'apellido', 'fecha_fallecimiento']

    template_name = 'cementerio/difuntos/difuntosmodificar.html'
