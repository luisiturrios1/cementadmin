# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.core.exceptions import ValidationError

from cementerio.models import Terreno


class ClientesAgregarTerrenoForm(forms.ModelForm):

    def clean_manzana(self):

        manzana = self.cleaned_data['manzana']

        if manzana is not None:
            manzana = manzana.upper()

        return manzana

    def clean(self):

        cleaned_data = super(ClientesAgregarTerrenoForm, self).clean()

        columna = cleaned_data['columna']

        lote = cleaned_data['lote']

        if columna is None and lote is not None:
            raise ValidationError(
                'Si ingresa un lote es obligatorio agregar una columna'
            )

        if lote is None and columna is not None:
            raise ValidationError(
                'Si ingresa una columna es obligatorio agregar un lote'
            )

        return cleaned_data

    class Meta:

        model = Terreno

        fields = [
            'tipo',
            'capacidad',
            'manzana',
            'columna',
            'lote',
            'notas'
        ]
