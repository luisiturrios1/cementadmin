# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from cementerio.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'direccion',
            'notas',
            'beneficiario_1',
            'beneficiario_2',
        ]
