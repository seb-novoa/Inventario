from django.db import models
from django.urls import reverse

class Puesto(models.Model):
    puesto  =   models.CharField(max_length = 30, unique = True)

    def __save__(self):
        self.puesto = self.puesto.lower()
        super(Puesto, self).save()

    def __str__(self):
        return self.puesto

    def get_absolute_url(self):
        pass
