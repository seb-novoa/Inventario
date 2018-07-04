from django.db import models

from Equipo.models import Equipo
from Personal.models import Personas

class PersonalEquipo(models.Model):
    persona    =   models.ForeignKey(Personas, on_delete = models.SET_NULL, null = True)
    equipos     =   models.ManyToManyField(Equipo)
    estado      =   models.BooleanField(default = True)
    fecha_inicio    =   models.DateTimeField(auto_now = True)
    fecha_termino   =   models.DateTimeField(auto_now = False)
