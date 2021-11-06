# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse


def recibo_pago_path(instance, filename):

    filename, ext = os.path.splitext(filename)

    path = 'recibo_pago/{0}-{1}-{2}.{3}'.format(
        instance.manzana,
        instance.columna,
        instance.lote,
        ext
    )

    return path


class Terreno(models.Model):

    tipo = models.CharField(max_length=2, default='TR', choices=(
        ('TR', u'Terreno regular'),
        ('GF', u'Gaveta Familiar'),
    ))

    capacidad = models.PositiveIntegerField(default=2, null=False, blank=False)

    manzana = models.CharField(max_length=20, null=False, blank=False)

    columna = models.PositiveIntegerField(null=True, blank=True, default=None)

    lote = models.PositiveIntegerField(null=True, blank=True, default=None)

    vendido = models.BooleanField(default=True, null=False, blank=False)

    perpetuidad = models.BooleanField(default=False, null=False, blank=False)

    cliente = models.ForeignKey(
        'cementerio.Cliente', related_name='terrenos',
        null=True, default=None, on_delete=models.CASCADE
    )

    notas = models.CharField(
        max_length=500, null=True, blank=True,
        verbose_name='Notas',
    )

    recibo_numero = models.CharField(max_length=10, null=True, blank=True)

    fecha_regitro = models.DateTimeField(auto_now_add=True)

    fecha_venta = models.DateField(null=True, default=None)

    creado_por = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )

    site = models.ForeignKey(
        Site, null=False, blank=False, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['manzana', 'columna', 'lote']

    def __str__(self):

        return self.__unicode__()

    def __unicode__(self):

        return u'{0}-{1}-{2}-{3}'.format(
            self.tipo, self.manzana,
            'XX' if self.columna is None else self.columna,
            'XX' if self.lote is None else self.lote
        )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.manzana = self.manzana.upper()

        if self.notas:

            self.notas = self.notas.upper()

        if self.recibo_numero:

            self.recibo_numero = self.recibo_numero.upper()

        super(Terreno, self).save(
            force_insert, force_update, using, update_fields
        )

    def get_absolute_url(self):

        return reverse('cementerio:terrenosdetalle', kwargs={'pk': self.pk})
