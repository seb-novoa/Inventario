from django.test import TestCase
from Personal.models import Puestos, Areas

class PuestoView(TestCase):
    def save_puesto(self, puesto):
        response = self.client.post('/persona/puesto/', data = {
            'Puesto' : puesto,
            'btn-guardar' : ['']
        })
        return response

    def test_PuestoView_render_template(self):
        response = self.client.get('/persona/puesto/')
        self.assertTemplateUsed(response, 'Personal/puesto.html')

    def test_PuestoView_create_a_puesto(self):
        response = self.save_puesto('puesto')
        self.assertEqual(Puestos.objects.count(), 1)

    def test_PuestoView_create_the_same(self):
        response = self.save_puesto('puesto')
        response = self.save_puesto('Puesto')
        self.assertEqual(Puestos.objects.count(), 1)

    def test_PuestoView_redirect_after_edit(self):
        puesto1 = self.save_puesto('puesto')

        puesto = Puestos.objects.first()
        response = self.client.post('/persona/puesto/{p}/'.format(p = puesto.id), data = {
            'Puesto'    :   'puesto2'
        })

        puesto = Puestos.objects.first()
        self.assertRedirects(response, '/persona/puesto/')
        self.assertEqual(puesto.Puesto, 'puesto2')

    def test_PuestoView_redirect_to_PuestoViewEditar(self):
        puesto1 = self.save_puesto('puesto1')
        response = self.client.post('/persona/puesto/', data = {
            'btn-editar' : ['1']
        })
        self.assertRedirects(response, '/persona/puesto/1/')

    def test_PuestoView_delete_a_puesto(self):
        puesto1 = self.save_puesto('puesto')
        self.assertContains(puesto1, 'Puesto')

        response = self.client.post('/persona/puesto/', data ={
            'btn-eliminar' : ['1']
        })
        self.assertEqual(Puestos.objects.count(), 0)

class AreaView(TestCase):
    def save_area(self, cdc, area):
        response = self.client.post('/persona/area/nueva/', data ={
            'CDC'   : cdc,
            'Area'  : area,
            'btn-guardar' : ['']
        })
        return response

    def test_AreaViewGuardar_render_template(self):
        response = self.client.get('/persona/area/nueva/')
        self.assertTemplateUsed(response, 'Personal/area-guardar.html')

    def test_AreaViewGuardar_create_an_area(self):
        response = self.save_area('ASDF1234', 'area1')
        self.assertEqual(Areas.objects.count(), 1)
        self.assertTemplateUsed(response, 'Personal/area-guardar.html')

    def test_AreaViewGuardar_dont_create_the_same_area(self):
        response = self.save_area('ASDF1234', 'Area1')
        response = self.save_area('ASDF1234', 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

    def test_AreaViewGuardar_dont_create_the_same_area_different_cdc(self):
        response = self.save_area('FDAS1234', 'Area1')
        response = self.save_area('ASDF1234', 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

    def test_AreaViewGuardar_dont_create_the_same_cdc_different_area(self):
        response = self.save_area('ASDF1234', 'Area1')
        response = self.save_area('ASDF1234', 'Area2')
        self.assertEqual(Areas.objects.count(), 1)

    def test_redirect_after_edit(self):
        area1 = self.save_area('ASDF1234', 'Area1')
        response = self.client.post('/persona/area/1/', data ={
            'CDC' : 'ZXCV1234',
            'Area': 'Area2'
        })

        area    =   Areas.objects.first()
        self.assertEqual(area.Area, 'area2')
        self.assertRedirects(response, '/persona/area/')

    def test_AreaView_redirect_to_AreaViewEditar(self):
        area1 = self.save_area('ASDF1234', 'Area1')
        response = self.client.post('/persona/area/', data = {
            'btn-editar'    :   ['1']
        })
        self.assertRedirects(response, '/persona/area/1/')

    def test_AreaView_delete_an_area(self):
        area1 = self.save_area('ASDF1234', 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

        response = self.client.post('/persona/area/', data ={
            'btn-eliminar' : ['1']
        })
        self.assertEqual(Areas.objects.count(), 0)
