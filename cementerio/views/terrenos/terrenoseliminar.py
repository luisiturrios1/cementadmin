# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from cementerio.models import Terreno


class TerrenosEliminar(PermissionRequiredMixin, DeleteView):

    permission_required = 'cementerio.delete_terreno'

    model = Terreno

    success_url = reverse_lazy('cementerio:terrenos')
