# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse


class Cliente(models.Model):

    nombre = models.CharField(max_length=50, null=False, blank=False)

    apellido = models.CharField(max_length=50, null=False, blank=False)

    telefono = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )

    direccion = models.CharField(
        max_length=200, null=True, blank=True, default=None
    )

    notas = models.CharField(
        max_length=500, null=True, blank=True, default='',
        verbose_name='Notas',
    )

    beneficiario_1 = models.CharField(
        max_length=200, null=True, blank=True, default=None
    )

    beneficiario_2 = models.CharField(
        max_length=200, null=True, blank=True, default=None
    )

    fecha_regitro = models.DateTimeField(auto_now_add=True)

    creado_por = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    site = models.ForeignKey(
        Site, null=False, blank=False, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return u'{0} {1}'.format(self.nombre, self.apellido)

    def __unicode__(self):
        return u'{0} {1}'.format(self.nombre, self.apellido)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()

        if self.telefono:
            self.telefono = self.telefono.upper()

        if self.direccion:
            self.direccion = self.direccion.upper()

        if self.notas:
            self.notas = self.notas.upper()

        if self.beneficiario_1:
            self.beneficiario_1 = self.beneficiario_1.upper()

        if self.beneficiario_2:
            self.beneficiario_2 = self.beneficiario_2.upper()

        super(Cliente, self).save(force_insert,
                                  force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('cementerio:clientesdetalle', kwargs={'pk': self.pk})
