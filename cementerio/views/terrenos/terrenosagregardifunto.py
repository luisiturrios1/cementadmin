# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views import View

from cementerio.forms import TerrenoAgregarDifuntoForm
from cementerio.models import Difunto, Terreno


class TerrenosAgregarDifunto(PermissionRequiredMixin, View):

    permission_required = 'cementerio.add_difunto'

    def get(self, request, pk):

        current_site = get_current_site(request)

        terreno = get_object_or_404(Terreno, pk=pk, site=current_site)

        form = TerrenoAgregarDifuntoForm()

        return render(
            request,
            'cementerio/terrenos/terrenosgregardifunto.html',
            {'terreno': terreno, 'form': form}
        )

    def post(self, request, pk):

        current_site = get_current_site(request)

        terreno = get_object_or_404(Terreno, pk=pk, site=current_site)

        difunto = Difunto(
            site=current_site,
            terreno=terreno,
            creado_por=request.user
        )

        form = TerrenoAgregarDifuntoForm(
            request.POST, instance=difunto
        )

        if form.is_valid():

            try:

                difunto = form.save()

                return HttpResponseRedirect(reverse('cementerio:terrenosdetalle', args=(terreno.pk,)))

            except Exception as e:

                form.add_error('__all__', e)

        return render(request, 'cementerio/terrenos/terrenosgregardifunto.html', {'form': form})
