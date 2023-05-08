# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View
# from elasticsearch_dsl import Q

# from cementerio.documents import DifuntoDocument
from cementerio.models import Difunto


class Difuntos(LoginRequiredMixin, View):

    def get(self, request):

        current_site = get_current_site(request)

        q = request.GET.get('q', '')

        if q == '':

            difuntos = Difunto.objects.filter(site=current_site)

        else:

            q = q.upper()

            difuntos = Difunto.objects.filter(site=current_site).filter(
                Q(nombre__icontains=q) | Q(apellido__icontains=q)
            )

            # query = Q("match", nombre={"query": q, "fuzziness": "2"}) | \
            #     Q("match", apellido={"query": q, "fuzziness": "2"})

            # difuntos = DifuntoDocument.search().query(
            #     query).to_queryset().filter(site=current_site)

        paginator = Paginator(difuntos, 25)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        return render(request, 'cementerio/difuntos/difuntos.html', {'page_obj': page_obj, 'q': q})
