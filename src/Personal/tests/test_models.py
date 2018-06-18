from django.test import TestCase

from Personal.models import Puestos, Areas, Personas

class PuestoModels(TestCase):
    def test_model_puesto_CAN_save(self):
        Puestos.objects.create(Puesto = 'Puesto1')
        self.assertEqual(Puestos.objects.count(), 1)

class AreaModels(TestCase):
    def test_model_area_CAN_save(self):
        Areas.objects.create(CDC = 'asdf1234', Area = 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

class PersonaModels(TestCase):
    def test_model_persona_CAN_save(self):
        area = Areas.objects.create(CDC = 'asdf1234', Area = 'Area1')
        puesto = Puestos.objects.create(Puesto = 'Puesto1')
        Personas.objects.create(Nombre = 'Nombre apellido apellido2', Area = area, Puesto = puesto)
        self.assertEqual(Personas.objects.count(), 1)
