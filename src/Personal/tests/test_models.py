from django.test import TestCase

from Personal.models import Puestos, Areas

class PuestoModels(TestCase):
    def test_model_puesto_CAN_save(self):
        Puestos.objects.create(Puesto = 'Puesto1')
        self.assertEqual(Puestos.objects.count(), 1)

class AreaModels(TestCase):
    def test_model_area_CAN_save(self):
        Areas.objects.create(CDC = 1, Area = 'Area1')
        self.assertEqual(Areas.objects.count(), 1)
