# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, render
from django.views import View

from cementerio.models import Difunto


class DifuntosDetalle(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):

        current_site = get_current_site(request)

        difunto = get_object_or_404(Difunto, pk=pk, site=current_site)

        return render(request, 'cementerio/difuntos/difuntosdetalle.html', {'difunto': difunto})
