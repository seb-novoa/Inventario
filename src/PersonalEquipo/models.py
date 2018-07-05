from django.db import models
from django.utils import timezone

from Equipo.models import Equipo
from Personal.models import Personas

class PersonalEquipo(models.Model):
    persona     =   models.ForeignKey(Personas, on_delete = models.SET_NULL, null = True)
    equipo      =   models.ForeignKey(Equipo, on_delete = models.SET_NULL, null = True)
    estado      =   models.BooleanField(default = False)
    atrasado    =   models.BooleanField(default = False)
    fecha_inicio    =   models.DateTimeField(auto_now = False, null = True)
    fecha_termino   =   models.DateTimeField(auto_now = False)

    def __str__(self):
        return '{0} - {1}'.format(self.persona, self.equipo)

    def atrasados(self):
        if self.fecha_termino < timezone.now():
            self.estado =   True
        else:
            self.estado =   False
        self.save()

    def alerta(self):
        return self.fecha_termino < timezone.now()

    def save(self):
        self.equipo.estado  =   False
        self.equipo.save()
        self.estado         =   True

        super(PersonalEquipo, self).save()
