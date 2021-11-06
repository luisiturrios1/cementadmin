# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from cementerio.models import Difunto


class DifuntosEliminar(PermissionRequiredMixin, DeleteView):

    permission_required = 'cementerio.delete_difunto'

    model = Difunto

    success_url = reverse_lazy('cementerio:difuntos')
