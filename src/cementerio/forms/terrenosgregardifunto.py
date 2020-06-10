# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from cementerio.models import Difunto


class TerrenoAgregarDifuntoForm(forms.ModelForm):
    class Meta:
        model = Difunto
        fields = [
            'nombre',
            'apellido',
            'fecha_fallecimiento',
        ]
