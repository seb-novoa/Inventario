from django.shortcuts import render, redirect
from django.views import View

from Personal.models import Puestos
from Personal.forms import(
    PuestosInputForm, PuestosInputFormEditar, PuestosInputFormGuardar,
    AreaInputForm, AreaInputFormGuardar
)

class PuestoView(View):
    def get(self, request, *args, **kwargs):
        form = PuestosInputForm()
        context = {
            'title': 'Puestos',
            'form' : form
        }
        return render(request, 'Personal/puesto.html', context)

    def post(self, request, *args, **kwargs):
        form = PuestosInputForm(request.POST)
        context = {
            'title': 'Puestos',
            'form' : form
        }
        if 'btn-guardar' in request.POST:
            form = PuestosInputFormGuardar(request.POST)
            if form.is_valid():
                new_puesto = form.cleaned_data.get('Puesto')
                obj, created = Puestos.objects.get_or_create(Puesto = new_puesto)
                if created:
                    context['title']= 'El puesto ha sido creado'
                else:
                    context['title']= 'El puesto "{i}" ya estaba registrado'.format(i = obj.Puesto)

        if 'btn-editar' in request.POST:
            form = PuestosInputForm(request.POST)
            if form.is_valid():
                new_puesto = form.cleaned_data.get('Puesto')
                instance = Puestos.objects.get(Puesto = new_puesto)
                return redirect(instance)

        if 'btn-eliminar' in request.POST:
            form = PuestosInputForm(request.POST)
            if form.is_valid():
                new_puesto = form.cleaned_data.get('Puesto')
                instance = Puestos.objects.get(Puesto = new_puesto)
                context['title'] = 'El puesto "{p}" ha sido eliminado.'.format(p = instance)
                instance.delete()

        return render(request, 'Personal/puesto.html', context)

class PuestoViewEditar(View):
    def get(self, request, puesto_id, *args, **kwargs):
        puesto = Puestos.objects.get(id  = puesto_id)
        form = PuestosInputFormEditar()
        context = {
            'title': 'Editar puesto "{p}"'.format(p = puesto),
            'form' : form
        }
        return render(request, 'Personal/editar-puesto.html', context)

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
                context['title']= 'El puesto no ha sido editado'
            else:
                return redirect('/persona/puesto/')
        return render(request, 'Personal/editar-puesto.html', context)

class AreaView(View):
    def context_contructor(*args, **kwargs):
        context = {
            'title' :   args[1],
            'form'  :   args[2]
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.context_contructor('Areas', AreaInputForm())
        return render(request, 'Personal/area.html', context)

    def post(self, request, *args, **kwargs):
        context = self.context_contructor('areas', AreaInputForm())
        if 'btn-guardar' in request.POST:
            form = AreaInputFormGuardar(request.POST)
            if form.is_valid():
                print('GG')
            context = self.context_contructor('areasss', form)
        return render(request, 'Personal/area.html', context)
