from django.db import models
from django.urls import reverse

class Puesto(models.Model):
    puesto  =   models.CharField(max_length = 30, unique = True)

    def __save__(self):
        self.puesto = self.puesto.lower()
        super(Puesto, self).save()

    def __str__(self):
        puesto = self.puesto[0].upper() + self.puesto[1:]
        return puesto

class Area(models.Model):
    cdc     =   models.CharField(max_length = 8, unique = True)
    area    =   models.CharField(max_length = 30, unique = True)

    def __save__(self):
        self.cdc    = self.cdc.upper()
        self.area   =   self.area.lower()
        super(Clase, self).save()

    def __str__(self):
        area    =   self.area[0].upper() + self.area[1:]
        return area

class Persona(models.Model):
    nombre  =   models.CharField(max_length = 50, unique = False)
    nombre_secundario   = models.CharField(max_length = 30, null = True, unique = False)
    apellido_paterno    =   models.CharField(max_length = 30, null = True, unique = False)
    apellido_materno    =   models.CharField(max_length = 30, null = True, unique = False)

    area    = models.ForeignKey(Area, on_delete = models.SET_NULL, null = True)
    puesto  = models.ForeignKey(Puesto, on_delete = models.SET_NULL, null = True)

    Gestor = models.BooleanField(default = False)
    GestorIdentificador  =   models.ForeignKey('self', null = True)
