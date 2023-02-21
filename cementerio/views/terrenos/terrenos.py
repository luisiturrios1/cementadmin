# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from cementerio.models import Terreno


class Terrenos(LoginRequiredMixin, View):

    def get(self, request):

        current_site = get_current_site(request)

        terrenos = Terreno.objects.filter(site=current_site)

        manzana = request.GET.get('manzana', None)

        if manzana:

            manzana = manzana.upper()

            terrenos = terrenos.filter(manzana=manzana)

        columna = request.GET.get('columna', None)

        if columna:

            terrenos = terrenos.filter(columna=columna)

        lote = request.GET.get('lote', None)

        if lote:

            lote = lote.upper()

            terrenos = terrenos.filter(lote=lote)

        paginator = Paginator(terrenos, 25)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        return render(request, 'cementerio/terrenos/terrenos.html', {
            'page_obj': page_obj,
            'manzana': manzana,
            'columna': columna,
            'lote': lote,
        })
