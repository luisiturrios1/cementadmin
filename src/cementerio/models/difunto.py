# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse


class Difunto(models.Model):

    nombre = models.CharField(max_length=50, null=False, blank=False)

    apellido = models.CharField(max_length=50, null=False, blank=False)

    fecha_fallecimiento = models.DateField(null=True, blank=True, default=None)

    terreno = models.ForeignKey(
        'cementerio.Terreno', related_name='difuntos', null=True, blank=True, default=None, on_delete=models.CASCADE
    )

    fecha_regitro = models.DateTimeField(auto_now_add=True)

    creado_por = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    site = models.ForeignKey(
        Site, null=False, blank=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return u'{0} {1}'.format(self.nombre, self.apellido)

    def __unicode__(self):
        return u'{0} {1}'.format(self.nombre, self.apellido)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.nombre = self.nombre.upper()

        self.apellido = self.apellido.upper()

        super(Difunto, self).save(
            force_insert, force_update, using, update_fields
        )

    def get_absolute_url(self):
        return reverse('cementerio:difuntosdetalle', kwargs={'pk': self.pk})
