from django.db import models
from django.urls import reverse

class Clase(models.Model):
    clase = models.CharField(max_length = 30, unique = True)

    def save(self, *args, **kwargs):
        self.clase = self.clase.lower()
        super(Clase, self).save(*args, **kwargs)

    def __str__(self):
        clase = self.clase[0].upper() + self.clase[1:]
        return clase

class Software(models.Model):
    software    =   models.CharField(max_length = 30,   unique=True)

    def save(self, *args, **kwargs):
        self.software = self.software.lower()
        super(Software, self).save(*args, **kwargs)

    def __str__(self):
        software = self.software[0].upper() + self.software[1:]
        return software

class Hardware(models.Model):
    hardware    =   models.CharField(max_length =   30, unique  =   True)
    descripcion =   models.CharField(max_length =   100,null = True)
    clases      =   models.ManyToManyField(Clase)

    def save(self, *args, **kwargs):
        self.hardware = self.hardware.lower()
        if self.descripcion:
            self.descripcion = self.descripcion.lower()
        super(Hardware, self).save(*args, **kwargs)

    def __str__(self):
        hardware = self.hardware[0].upper() + self.hardware[1:]
        return hardware


class Equipo(models.Model):
    serie   =   models.CharField(max_length = 30, unique = True)
    serieProveedor  =   models.CharField(max_length = 30, null = True, unique = True, blank = True)
    serieEnap   =   models.CharField(max_length = 30, null = True, unique = True, blank = True)
    estado  =   models.BooleanField(default = True)
    clase   =   models.ForeignKey(Clase, on_delete = models.SET_NULL, null = True)
    hardware    =   models.ManyToManyField(Hardware, blank = True)
    software    =   models.ManyToManyField(Software, blank = True)

    class Meta:
        ordering = ['-estado']

    def save(self):
        self.serie  =   self.serie.upper()

        if self.serieEnap:
            self.serieEnap =   self.serieEnap.upper()
        if self.serieProveedor:
            self.serieProveedor =   self.serieProveedor.upper()
        super(Equipo, self).save()

    def __str__(self):
        return '{0} {1}'.format(self.serie, self.clase)

    def get_absolute_url(self):
        return reverse('DetailEquipo', args =  [self.id])

class MAC(models.Model):
    mac     =   models.CharField(max_length = 17, unique = True)           # ([0-9A-F]{2}[:-]){5}([0-9A-F]{2})
    descripcion =   models.CharField(max_length = 30, null = True)
    equipo  =   models.ForeignKey(Equipo, on_delete = models.SET_NULL, null = True)

    def save(self):
        self.mac = self.mac.upper()

        if self.descripcion:
            self.descripcion = self.descripcion.lower()
        super(MAC, self).save()

    def __str__(self):
        return self.mac
