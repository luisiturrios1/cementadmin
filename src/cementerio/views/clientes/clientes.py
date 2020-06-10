# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from cementerio.models import Cliente


class Clientes(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        current_site = get_current_site(request)

        q = request.GET.get('q', None)

        if q == None:

            clientes = Cliente.objects.filter(site=current_site)

        else:

            clientes = Cliente.objects.filter(site=current_site).filter(
                Q(nombre__icontains=q) | Q(apellido__icontains=q)
            )        

        return render(request, 'cementerio/clientes/clientes.html', {'clientes': clientes})
