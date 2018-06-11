from django.test import TestCase
from Personal.models import Puestos

class PuestoView(TestCase):
    def test_PuestoView_render_template(self):
        response = self.client.get('/persona/puesto/')
        self.assertTemplateUsed(response, 'Personal/puesto.html')

    def test_PuestoView_create_a_puesto(self):
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : 'puesto'
        })
        self.assertEqual(Puestos.objects.count(), 1)

    def test_PuestoView_create_the_same(self):
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : 'puesto'
        })
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : 'Puesto'
        })
        self.assertEqual(Puestos.objects.count(), 1)
