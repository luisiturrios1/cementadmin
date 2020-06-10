# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views import View

from cementerio.forms import ClientesAgregarTerrenoForm
from cementerio.models import Cliente, Terreno


class ClientesAgregarTerreno(PermissionRequiredMixin, View):

    permission_required = 'cementerio.add_terreno'

    def get(self, request, pk):

        current_site = get_current_site(request)

        cliente = get_object_or_404(Cliente, pk=pk, site=current_site)

        form = ClientesAgregarTerrenoForm()

        return render(
            request,
            'cementerio/clientes/clientesagregarterreno.html',
            {'cliente': cliente, 'form': form}
        )

    def post(self, request, pk):

        current_site = get_current_site(request)

        cliente = get_object_or_404(Cliente, pk=pk, site=current_site)

        terreno = Terreno(
            site=current_site,
            cliente=cliente,
            creado_por=request.user,
        )

        form = ClientesAgregarTerrenoForm(
            request.POST, instance=terreno
        )

        if form.is_valid():

            columna = form.cleaned_data.get('columna', None)

            lote = form.cleaned_data.get('lote', None)

            if columna is None and lote is None:

                terreno = None

            else:

                # Revisar si el terreno esta dado de alta
                terreno = Terreno.objects.filter(
                    manzana=form.cleaned_data['manzana'],
                    columna=columna,
                    lote=lote,
                    site=current_site
                ).first()

            if terreno != None:

                form.add_error(
                    '__all__',
                    'Este terreno ya existe y pertenece a {0}'.format(
                        terreno.cliente
                    )
                )

            else:

                try:

                    terreno = form.save()

                    return HttpResponseRedirect(reverse('cementerio:terrenosdetalle', args=(terreno.pk,)))

                except Exception, e:

                    form.add_error('__all__', e)

        return render(
            request,
            'cementerio/clientes/clientesagregarterreno.html',
            {'cliente': cliente, 'form': form}
        )
