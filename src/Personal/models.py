from django.db import models
from django.urls import reverse

from .validators import value_is_lowercase

class Puestos(models.Model):
    Puesto = models.CharField(max_length = 30, unique = True, validators = [value_is_lowercase])

    def save(self, *args, **kwargs):
        super(Puestos, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Puesto)

    def get_absolute_url(self):
        return reverse('PuestoViewEditar', args = [self.id])
