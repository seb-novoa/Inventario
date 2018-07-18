from django.db import models
from django.urls import reverse
from django.utils import timezone

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
    apellido_paterno    =   models.CharField(max_length = 30, null = True, unique = False)
    apellido_materno    =   models.CharField(max_length = 30, null = True, unique = False)

    area    = models.ForeignKey(Area, on_delete = models.SET_NULL, null = True)
    puesto  = models.ForeignKey(Puesto, on_delete = models.SET_NULL, null = True)

    Gestor = models.BooleanField(default = False)
    GestorIdentificador  =   models.ForeignKey('self',  on_delete = models.SET_NULL, null = True)

    def __save__(self):
        self.nombre =   self.nombre.lower()
        self.apellido_paterno   =   self.apellido_paterno.lower()
        self.apellido_materno   =   self.apellido_materno.lower()
        super(Persona, self).save()

    def __str__(self):
        return '{0} {1} del área {2}'.format(self.nombre, self.apellido_paterno, self.area)

    def get_absolute_url(self):
        return reverse('PersonaDetail', args = [self.id])

    def total_equipos(self):
        return self.personalequipo_set.all().count() + self.persona_set.filter(personalequipo__estado=True).count()

    def total_equipos_vencidos(self):
        total = 0
        for date in self.personalequipo_set.values('fecha_termino'):
            if timezone.now().date() > date.get('fecha_termino').date():
                total   +=  1
        for persona in self.persona_set.all():
            for date in persona.personalequipo_set.values('fecha_termino'):
                if timezone.now().date() > date.get('fecha_termino').date():
                    total   +=  1
        return total
