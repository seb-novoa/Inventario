from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from Equipo.models import Equipo, MAC
from Equipo.Equipo.forms import EquipoCreateForm, CreateMacForm, UpdateMACForm, EquipoHardwareForm, EquipoSoftwareForm, EquipoUpdateForm, BuscarEquipoForm

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
        if 'btn-cancelar' in request.POST:
            return redirect('BuscarEquipo')
        form        =   EquipoCreateForm(request.POST)
        if form.is_valid():
            instance    =   form.save()
            print(instance)
            return redirect(instance)

        context     =   self.context_data(form = form)
        return render(request, self.template_name, context)

class BuscarEquipo(CreateEquipo):
    template_name   =   'Equipo/buscar_equipo.html'
    title           =   'Buscar Equipo'

    def get_object(self, equipo):
        equipo = equipo.upper()
        equipos     =   Equipo.objects.all()
        if equipos.filter(serie = equipo):
            return equipos.get(serie = equipo)
        elif equipos.filter(serieEnap = equipo):
            return equipos.get(serieEnap = equipo)
        elif equipos.filter(serieEntel = equipo):
            return equipos.get(serieEntel = equipo)
        else:
            e   =   MAC.objects.get(mac = equipo)
            return e.equipo

    def get(self, request):
        context     =   self.context_data(form = BuscarEquipoForm(), title = self.title)
        return render(request, self.template_name, context)

    def post(self, request):
        form        =   BuscarEquipoForm(request.POST)
        context     =   self.context_data(form = form, title = self.title )
        if form.is_valid():
            if not form.cleaned_data['serie']:
                context['clase']    =   form.cleaned_data['clase']
            if form.cleaned_data['serie']:
                equipo  =   self.get_object(form.cleaned_data['serie'])
                return redirect(equipo)

        return render(request, self.template_name, context)

class UpdateEquipo(CreateEquipo):
    def get(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)
        context     =   self.context_data(form = EquipoUpdateForm(instance = instance), title = 'Editar Equipo')
        return render(request, self.template_name, context)

    def post(self, request, pk):
        instance    =   get_object_or_404(Equipo, id = pk)

        if 'btn-cancelar' in request.POST:
            return redirect(instance)
        form        =   EquipoUpdateForm(request.POST or None, instance = instance)
        if form.is_valid():
            form.save()
            return redirect(instance)
        context     =   self.context_data(form = form, title = 'Editar equipo')
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
