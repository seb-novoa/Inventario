from django.db import models
from django.urls import reverse

from .validators import value_is_lowercase, value_is_correct_expression_regular

class Puestos(models.Model):
    Puesto = models.CharField(max_length = 30, unique = True, validators = [value_is_lowercase])

    def save(self, *args, **kwargs):
        super(Puestos, self).save(*args, **kwargs)

    def __str__(self):
        puestolow = self.Puesto
        puesto = puestolow[0].upper() + puestolow[1:]
        return str(puesto)

    def get_absolute_url(self):
        return reverse('PuestoViewEditar', args = [self.id])

class Areas(models.Model):
    CDC     = models.CharField(max_length = 8, unique = True, validators = [value_is_correct_expression_regular])
    Area    = models.CharField(max_length = 30, unique = True)

    def save(self, *args, **kwargs):
        self.CDC = self.CDC.upper()
        super(Areas, self).save(*args, **kwargs)


    def __str__(self):
        arealow = self.Area
        area = arealow[0].upper() + arealow[1:]
        return area

    def get_absolute_url(self):
        return reverse('AreaViewEditar', args = [self.id])
