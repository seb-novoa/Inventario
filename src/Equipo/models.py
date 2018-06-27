from django.db import models

class Clase(models.Model):
    clase = models.CharField(max_length = 30, unique = True)

    def save(self, *args, **kwargs):
        self.clase = self.clase.lower()
        super(Clase, self).save(*args, **kwargs)

    def __str__(self):
        clase = self.clase[0].upper() + self.clase[1:]
        return clase
