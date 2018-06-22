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
        self.Area = self.Area.lower()
        super(Areas, self).save(*args, **kwargs)

    def area_str(self):
        self.Area = self.Area[0].upper() + self.Area[1:]
        return self.Area

    def __str__(self):
        self.Area = self.Area[0].upper() + self.Area[1:]
        return self.Area

    def get_absolute_url(self):
        return reverse('AreaViewEditar', args = [self.id])

class Personas(models.Model):
    Nombre  =   models.CharField(max_length = 50, unique = False)
    NombreSecundario = models.CharField(max_length = 30, null = True, unique = False)
    Apellido    =   models.CharField(max_length = 30, null = True, unique = False)
    ApellidoMaterno =   models.CharField(max_length = 30, null = True, unique = False)

    Area = models.ForeignKey(Areas, on_delete = models.CASCADE)
    Puesto = models.ForeignKey(Puestos, on_delete = models.CASCADE)

    Gestor = models.BooleanField(default = False)
    GestorIdentificador  =   models.ForeignKey('self', null = True)


    def split_Nombre(self, nom):
        nombre = nom.split()
        if len(nombre) == 3:
            self.Nombre = nombre[0]
            self.Apellido = nombre[1]
            self.ApellidoMaterno = nombre[2]

        elif len(nombre) > 3:
            self.Nombre = nombre[0]
            self.NombreSecundario = nombre[1]
            self.Apellido = nombre[2]
            self.ApellidoMaterno = ''.join(nombre[3:])

    def save(self, *args, **kwargs):
        self.split_Nombre(self.Nombre)
        super(Personas, self).save(*args, **kwargs)

    def gestor(self):
        self.Gestor = True
        self.save()

    def __str__(self):
        return '{0} {1} del area {2}'.format(self.Nombre, self.Apellido, self.Area)

    def get_absolute_url(self):
        return reverse('PersonaViewGestor', args = [self.id])

    def get_gestor_url(self):
        gestor = self.GestorIdentificador
        return reverse('PersonaViewDetail', args=[self.GestorIdentificador])
