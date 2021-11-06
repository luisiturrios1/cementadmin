# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views import View

from cementerio.models import Terreno


class Terrenos(LoginRequiredMixin, View):

    def get(self, request):

        current_site = get_current_site(request)

        terrenos = Terreno.objects.filter(site=current_site)

        manzana = request.GET.get('manzana', None)

        if manzana:

            terrenos = terrenos.filter(manzana=manzana)

        columna = request.GET.get('columna', None)

        if columna:

            terrenos = terrenos.filter(columna=columna)

        lote = request.GET.get('lote', None)

        if lote:

            terrenos = terrenos.filter(lote=lote)

        return render(request, 'cementerio/terrenos/terrenos.html', {'terrenos': terrenos})
