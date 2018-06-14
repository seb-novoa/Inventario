from django.test import TestCase
from Personal.models import Puestos, Areas

class PuestoView(TestCase):
    def test_PuestoView_render_template(self):
        response = self.client.get('/persona/puesto/')
        self.assertTemplateUsed(response, 'Personal/puesto.html')

    def test_PuestoView_create_a_puesto(self):
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : 'puesto',
            'btn-guardar' : ['']
        })
        self.assertEqual(Puestos.objects.count(), 1)

    def test_PuestoView_create_the_same(self):
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : 'puesto'
        })
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : 'Puesto',
            'btn-guardar' : ['']
        })
        self.assertEqual(Puestos.objects.count(), 1)

class AreaView(TestCase):
    def test_AreaViewGuardar_render_template(self):
        response = self.client.get('/persona/area/nueva/')
        self.assertTemplateUsed(response, 'Personal/area-guardar.html')

    def test_AreaViewGuardar_create_an_area(self):
        response = self.client.post('/persona/area/nueva/', data ={
            'CDC'   : 'ASDF1234',
            'Area'  : 'Area1',
            'btn-guardar' : ['']
        })
        self.assertEqual(Areas.objects.count(), 1)
