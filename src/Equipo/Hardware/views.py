from django.shortcuts import render, redirect
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

    def context_data(self, form = HardwareCreateForm()):
        context = {
            'form'  :   form,
            'programas' :   self.all_hardware()
        }
        return context

    def get(self, request):
        context = self.context_data()
        
        return render(request, self.template_name, context)

class CreateHardware(HardwareView):
    template_name   =   'Hardware/hardware_create_form.html'





    def get(self, request):
        context = self.context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        if 'btn-cancelar' in request.POST:
            return redirect('HardwareView')

        form = HardwareCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado el hardware', extra_tags='alert alert-success')
            return redirect('HardwareView')
        context = self.context_data(form = form)
        return render(request, self.template_name, context)
