from django.test import TestCase

from Personal.models import Puestos

class PuestoModels(TestCase):
    def test_model_puesto_CAN_save(self):
        Puestos.objects.create(Puesto = 'Puesto1')
        self.assertEqual(Puestos.objects.count(), 1)
