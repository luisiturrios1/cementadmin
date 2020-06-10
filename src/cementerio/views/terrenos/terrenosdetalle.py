# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, render
from django.views import View

from cementerio.models import Terreno


class TerrenosDetalle(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):

        current_site = get_current_site(request)

        terreno = get_object_or_404(Terreno, pk=pk, site=current_site)

        return render(request, 'cementerio/terrenos/terrenosdetalle.html', {'terreno': terreno})
