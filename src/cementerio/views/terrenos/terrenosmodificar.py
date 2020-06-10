# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView

from cementerio.models import Terreno


class TerrenosModificar(PermissionRequiredMixin, UpdateView):

    permission_required = 'cementerio.change_terreno'

    model = Terreno

    fields = ['beneficiario']

    template_name = 'cementerio/terrenos/terrenosmodificar.html'
