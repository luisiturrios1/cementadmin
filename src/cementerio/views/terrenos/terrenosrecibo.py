# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import HttpResponse, get_object_or_404
from django.utils.encoding import smart_str
from django.views import View

from cementerio.models import Terreno


class TerrenosRecibo(LoginRequiredMixin, View):
    def get(self, request, pk):

        current_site = get_current_site(request)

        terreno = get_object_or_404(Terreno, pk=pk, site=current_site)

        response = HttpResponse(
            terreno.recibo_pago.read(), content_type='application/force-download'
        )

        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(
            terreno.recibo_pago.name
        )

        response['X-Sendfile'] = smart_str(terreno.recibo_pago.path)

        return response
