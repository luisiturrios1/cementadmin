# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views import View

from cementerio.models import Cliente, Difunto, Terreno


class Inicio(LoginRequiredMixin, View):

    def get(self, request):

        current_site = get_current_site(request)

        data = {
            'terrenos': Terreno.objects.filter(site=current_site).count(),
            'clientes': Cliente.objects.filter(site=current_site).count(),
            'difuntos': Difunto.objects.filter(site=current_site).count(),
        }

        return render(request, 'cementerio/inicio.html', data)
