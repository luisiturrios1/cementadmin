# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cliente, Difunto, Terreno


class TerrenoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


class DifuntoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Terreno, TerrenoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Difunto, DifuntoAdmin)
