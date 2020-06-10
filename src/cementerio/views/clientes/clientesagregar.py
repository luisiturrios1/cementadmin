# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, render
from django.views import View

from cementerio.forms import ClienteForm
from cementerio.models import Cliente


class ClientesAgregar(PermissionRequiredMixin, View):

    permission_required = 'cementerio.add_cliente'

    def get(self, request, *args, **kwargs):

        form = ClienteForm()

        return render(request, 'cementerio/clientes/clientesagregar.html', {'form': form})

    def post(self, request, *args, **kwargs):

        current_site = get_current_site(request)

        cliente = Cliente(
            site=current_site,
            creado_por=request.user
        )

        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():

            try:

                cliente = form.save()

                return HttpResponseRedirect(reverse('cementerio:clientesdetalle', args=(cliente.pk,)))

            except Exception, e:

                form.add_error('__all__', e)

        return render(request, 'cementerio/clientes/clientesagregar.html', {'form': form})
