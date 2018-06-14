from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

import re

from Personal.models import Puestos, Areas
from Personal.forms import(
    PuestosInputForm, PuestosInputFormEditar, PuestosInputFormGuardar,
    AreaInputForm, AreaInputFormBuscar
)

class PuestoView(View):
    def all_puestos(self):
        return Puestos.objects.all()

    def context_contructor(self, title, form):
        context = {
            'title' :   title,
            'form'  :   form
        }
        return context

    def get(self, request, *args, **kwargs):
        form = PuestosInputForm()
        context = self.context_contructor('Puestos', form)
        context['puestos'] = self.all_puestos()
        return render(request, 'Personal/puesto.html', context)

    def post(self, request, *args, **kwargs):
        form = PuestosInputForm()
        context = self.context_contructor('Puestos', form)
        if 'btn-guardar' in request.POST:
            form = PuestosInputFormGuardar(request.POST)
            if form.is_valid():
                new_puesto = form.cleaned_data.get('Puesto')
                obj, created = Puestos.objects.get_or_create(Puesto = new_puesto)
                if created:
                    messages.success(request, 'El puesto "{p}" ha sido creado'.format(p = obj.Puesto))
                else:
                    context['obj']= obj

        if 'btn-editar' in request.POST:
            new_puesto = request.POST.get('btn-editar')
            instance = Puestos.objects.get(id = new_puesto)
            return redirect(instance)

        if 'btn-eliminar' in request.POST:
            del_puesto = request.POST.get('btn-eliminar')
            instance = Puestos.objects.get(id = del_puesto)
            messages.success(request, 'El puesto "{p}" ha sido eliminado.'.format(p = instance))
            instance.delete()
        context['puestos'] = self.all_puestos()
        return render(request, 'Personal/puesto.html', context)

class PuestoViewEditar(View):
    def get(self, request, puesto_id, *args, **kwargs):
        puesto = Puestos.objects.get(id  = puesto_id)
        form = PuestosInputFormEditar()
        context = {
            'title': 'Editar puesto "{p}"'.format(p = puesto),
            'form' : form
        }
        return render(request, 'Personal/puesto-editar.html', context)

    def post(self, request, puesto_id, *args, **kwargs):
        form = PuestosInputFormEditar(request.POST)
        puesto = Puestos.objects.get(id  = puesto_id)
        context = {
            'title': 'Editar puesto "{p}"'.format(p = puesto),
            'form' : form
        }
        if form.is_valid():
            new_puesto = form.cleaned_data.get('Puesto')
            obj, created = Puestos.objects.update_or_create(defaults = {'Puesto' : new_puesto},  id= puesto_id)
            if created:
                messages.error(request, 'El puesto no ha sido creado')
            else:
                messages.success(request, 'El puesto se ha guardado')
                return redirect('/persona/puesto/')
        return render(request, 'Personal/puesto-editar.html', context)

class AreaView(View):
    def context_contructor(self, title, form):
        context = {
            'title' :   title,
            'form'  :   form
        }
        return context

    def objecto(self, value):
        patron = re.compile('^[A-Z]{4}[0-9]{4}$')
        if patron.match(value.upper()):
            obj = Areas.objects.get(CDC = value)
        else:
            obj = Areas.objects.get(Area = value)

        return obj

    def all_areas(self):
        areas = Areas.objects.all()
        return areas

    def get(self, request, *args, **kwargs):
        context = self.context_contructor('Areas', AreaInputFormBuscar())
        context['areas'] = self.all_areas()
        return render(request, 'Personal/area.html', context)

    def post(self, request, *args, **kwargs):
        context = self.context_contructor('Areas', AreaInputFormBuscar())


        if 'btn-buscar' in request.POST:
            form = AreaInputFormBuscar(request.POST)
            context = self.context_contructor('Area buscando....', form)
            if form.is_valid():
                obj = self.objecto(form.cleaned_data.get('Buscar'))
                context['obj'] = obj

        if 'btn-editar' in request.POST:
            new_area = request.POST.get('btn-editar')
            instance = Areas.objects.get(id = new_area)
            return redirect(instance)

        if 'btn-eliminar' in request.POST:
            del_area = request.POST.get('btn-eliminar')
            instance = Areas.objects.get(id = del_area)
            messages.success(request, 'El area "{p}" ha sido eliminado.'.format(p = instance))
            instance.delete()

        context['areas'] = self.all_areas()
        return render(request, 'Personal/area.html', context)

class AreaViewEditar(AreaView):
    def get(self, request, area_id, *args, **kwargs):
        form  = AreaInputForm
        instance = Areas.objects.get(id = area_id)
        context = self.context_contructor('Editar área {i}'.format(i = instance.Area), form)
        return render(request, 'Personal/area-guardar.html', context)

    def post(self, request, area_id, *args, **kwargs):
        form = AreaInputForm(request.POST)
        area = Areas.objects.get(id  = area_id)
        context = self.context_contructor('Editar área {i}'.format(i = area), form)

        if form.is_valid():
            new_area = form.cleaned_data.get('Area')
            new_cdc = form.cleaned_data.get('CDC')
            obj, created = Areas.objects.update_or_create(defaults = {'Area' : new_area, 'CDC': new_cdc},  id= area_id)
            if created:
                messages.error(request, 'El area no ha sido creado')
            else:
                messages.success(request, 'El area se ha guardado')
                return redirect('/persona/area/')
        return render(request, 'Personal/area-guardar.html', context)

class AreaViewGuardar(AreaView):
    template = 'Personal/area-guardar.html'

    def correct_field(self, cdc, area):
        cdc_field = Areas.objects.filter(CDC = cdc) or False
        area_field = Areas.objects.filter(Area = area) or False
        return [cdc_field, area_field]

    def get(self, request, *args, **kwargs):
        context = self.context_contructor('Crear Area', AreaInputForm())
        return render(request, self.template, context)


    def post(self, request, *args, **kwargs):
        form = AreaInputForm(request.POST)
        context = self.context_contructor('Area', form)
        if form.is_valid():
            new_area = [form.cleaned_data.get('CDC'), form.cleaned_data.get('Area')]
            obj, created = Areas.objects.get_or_create(CDC = new_area[0], Area = new_area[1])

            if created:
                context= self.context_contructor('Area', form)
                messages.success(request, 'El área ha sido creada')
                context['area'] = obj
            else:
                context= self.context_contructor('Area', form)
                context['area'] = obj
        else:
            cdc = request.POST.get('CDC')
            area = request.POST.get('Area')
            correct = self.correct_field(cdc, area)
            if correct[0]:
                context['area'] = Areas.objects.get(CDC = cdc)
            elif correct[1]:
                context['area'] = Areas.objects.get(Area = area)

        return render(request, self.template, context)
