from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from Equipo.models import Equipo, MAC
from Equipo.Equipo.forms import EquipoCreateForm, CreateMacForm, UpdateMACForm, EquipoHardwareForm, EquipoSoftwareForm

# CreateEquipo

class CreateEquipo(View):
    template_name   =   'base_crear.html'

    def context_data(self, form = EquipoCreateForm(), title = 'Agregar Equipo'):
        return {
            'title' :   title,
            'form'  :   form
        }

    def get(self,  request):
        context     =   self.context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        # if 'btn-cancelar' in request.POST:
        #     return redirect()
        form        =   EquipoCreateForm(request.POST)
        if form.is_valid():
            instance    =   form.save()
            print(instance)
            return redirect(instance)

        context     =   self.context_data(form = form)
        return render(request, self.template_name, context)

class DetailEquipo(CreateEquipo):
    template_name   =   'Equipo/detail_equipo.html'

    def get(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        return render(request, self.template_name, {'equipo'    :   instance})

class addMAC(CreateEquipo):
    def get(self, request, pk):
        context     =   self.context_data(form = CreateMacForm(), title = 'Agregar tarjeta de red')
        return render(request, self.template_name, context)

    def post(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        if 'btn-cancelar' in request.POST:
            return redirect(instance)
        form    =   CreateMacForm(request.POST)
        if form.is_valid():
            mac =   form.save()
            mac.equipo  =   instance
            mac.save()
            return redirect(instance)

        context =   self.context_data(form = form, title = 'Agregar tarjeta de red')
        return render(request, self.template_name, context)

class EditarMAC(addMAC):
    def get(self, request, pk):
        instance    =   get_object_or_404(MAC, id = pk)
        context     =   self.context_data(form = UpdateMACForm(instance = instance), title = 'Editar tarjeta de red')
        return render(request, self.template_name, context)

    def post(self, request, pk):
        instance    =   get_object_or_404(MAC, id = pk)
        if 'btn-cancelar' in request.POST:
            return redirect(instance.equipo)
        form    =   UpdateMACForm(request.POST or None, instance = instance)
        if form.is_valid():
            form.save()
            return redirect(instance.equipo)

        context     =   self.context_data(form = form, title = 'Editar tarjeta de red')
        return render(request, self.template_name, context)

class DeleteMAC(View):
    def post(self, request, pk):
        instance    =   get_object_or_404(MAC, id = pk)
        obj         =   instance.equipo
        instance.delete()
        return redirect(obj)

class EquipoHardware(CreateEquipo):
    def get(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        context     =   self.context_data(form = EquipoHardwareForm(instance = instance), title = 'Hardware')
        return render(request, self.template_name, context )

    def post(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        form        =   EquipoHardwareForm(request.POST or None, instance = instance)
        if 'btn-cancelar' in request.POST:
            return redirect(instance)
        context     =   self.context_data(form = form)

        if form.is_valid():
            form.save()
            return redirect(instance)

        return render(request, self.template_name, context )

class EquipoSoftware(CreateEquipo):
    def get(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        context     =   self.context_data(form = EquipoSoftwareForm(instance = instance), title = 'Software')
        return render(request, self.template_name, context )

    def post(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        form        =   EquipoSoftwareForm(request.POST or None, instance = instance)
        if 'btn-cancelar' in request.POST:
            return redirect(instance)
        context     =   self.context_data(form = form)

        if form.is_valid():
            form.save()
            return redirect(instance)

        return render(request, self.template_name, context )
