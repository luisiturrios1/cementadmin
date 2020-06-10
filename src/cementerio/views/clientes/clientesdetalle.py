# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, render
from django.views import View

from cementerio.models import Cliente


class ClientesDetalle(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):

        current_site = get_current_site(request)

        cliente = get_object_or_404(Cliente, pk=pk, site=current_site)

        return render(request, 'cementerio/clientes/clientesdetalle.html', {'cliente': cliente})
