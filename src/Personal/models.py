from django.db import models

from .validators import value_is_lowercase

class Puestos(models.Model):
    Puesto = models.CharField(max_length = 30, unique = True, validators = [value_is_lowercase])

    def __str__(self):
        return str(self.Puesto)
