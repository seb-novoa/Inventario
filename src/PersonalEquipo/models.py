from django.db import models
from django.utils import timezone

from Equipo.models import Equipo
# from Personal.models import Personas

class PersonalEquipo(models.Model):
    # persona         =   models.ForeignKey(Personas, on_delete = models.SET_NULL, null = True)
    equipo          =   models.ForeignKey(Equipo, on_delete = models.SET_NULL, null = True)
    estado          =   models.BooleanField(default = False)
    fecha_inicio    =   models.DateTimeField(auto_now = False, null = True)
    fecha_termino   =   models.DateTimeField(auto_now = False)

    def __str__(self):
        return '{0} - {1}'.format(self.persona, self.equipo)


    def atrasados(self):
        if self.fecha_termino < timezone.now():
            return True
        return False


    def alerta(self):
        return timezone.now().date() >  self.fecha_termino.date()

    def save(self):
        self.equipo.estado  =   False
        self.equipo.save()
        self.estado         =   True

        super(PersonalEquipo, self).save()

class PersonalEquipoHistoria(models.Model):
    fecha_entrega   =   models.DateTimeField(auto_now = False, null = True)
    # persona         =   models.ForeignKey(Personas, on_delete = models.SET_NULL, null = True )
    equipo          =   models.ForeignKey(Equipo, on_delete = models.SET_NULL, null = True)
    fecha_inicio    =   models.DateTimeField(auto_now = False )
    fecha_termino   =   models.DateTimeField(auto_now = False )
    hw              =   models.CharField(max_length = 100 )
    sw              =   models.CharField(max_length = 100 )

    def __str__(self):
        return '{0} - {1} entregado entre {2} al {3}'.format(self.persona, self.equipo, self.fecha_inicio.date(), self.fecha_entrega.date())
