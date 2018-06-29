from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from Equipo.models import Hardware, Clase
from Equipo.Hardware.forms import HardwareCreateForm

# HardwareView
# CreateHardware

class HardwareView(View):
    template_name   =   'Hardware/hardware.html'

    def all_hardware(self):
        return Hardware.objects.all()

    def context_data(self, form = HardwareCreateForm(), title = None):
        context = {
            'form'  :   form,
            'programas' :   self.all_hardware(),
            'title'     :   title
        }
        return context

    def get(self, request):
        context = self.context_data()

        return render(request, self.template_name, context)

class CreateHardware(HardwareView):
    template_name   =   'Hardware/hardware_create_form.html'
    title           =   'Registrar hardware'

    def get(self, request):
        context = self.context_data(title = self.title)
        return render(request, self.template_name, context)

    def post(self, request):
        if 'btn-cancelar' in request.POST:
            return redirect('HardwareView')

        form = HardwareCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado el hardware', extra_tags='alert alert-success')
            return redirect('HardwareView')
        context = self.context_data(form = form, title = self.title)
        return render(request, self.template_name, context)

# UpdateHardware
class UpdateHardware(CreateHardware):
    title = 'Editar hardware'
    def get(self, request, pk):
        instance    =   get_object_or_404(Hardware, id = pk)
        context     =   self.context_data(form = HardwareCreateForm(instance = instance), title = self.title)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        if 'btn-cancelar' in request.POST:
            return redirect('HardwareView')

        instance    =   get_object_or_404(Hardware, id = pk)
        form        =   HardwareCreateForm(request.POST or None, instance = instance)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se edito el hardware', extra_tags = 'alert alert-success')
            return redirect('HardwareView')

        context     =   self.context_data(form = form, title = self.title)
        return render(request, self.template_name, context)
