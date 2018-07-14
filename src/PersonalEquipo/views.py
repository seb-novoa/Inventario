from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils import timezone

#   Modelos
# from Personal.models import Personas
from Equipo.models import Equipo
from PersonalEquipo.models import PersonalEquipo, PersonalEquipoHistoria

#   forms
from PersonalEquipo.forms import RelacionForm

class Asignar(View):
    template_name       =   'base_crear.html'
    def context_data(self, form = RelacionForm(), title = 'Asignar Equipo'):
        return {
            'title'     :   title,
            'form'      :   form
        }


    def get(self, request, pk):
        context     =   self.context_data()
        return render(request, self.template_name, context)

    def post(self, request, pk):
        persona     =   get_object_or_404(Personas, id = pk)
        if 'btn-cancelar' in request.POST:
            return redirect('PersonaViewDetail', pk)
        form        =   RelacionForm(request.POST)

        if form.is_valid():
            r       =   form.save()
            r.persona   =   persona
            r.fecha_inicio  =   timezone.now().date()
            r.save()
            return redirect('PersonaViewDetail', pk)
        context     =   self.context_data(form = form)
        return render(request, self.template_name, context)

class Devolver(View):
    def post(self, request, pk):
        instance    =   get_object_or_404(PersonalEquipo, id = pk)

        hw  =   ''
        sw  =   ''
        for hardware in instance.equipo.hardware.all():
            hw += str(hardware) + ' '
        for software in instance.equipo.software.all():
            sw  +=  str(software) + ' '

        historial   =   PersonalEquipoHistoria()
        historial.fecha_entrega =   timezone.now()
        historial.persona       =   instance.persona
        historial.equipo        =   instance.equipo
        historial.fecha_inicio  =   instance.fecha_inicio
        historial.fecha_termino =   instance.fecha_termino
        historial.hw            =   hw
        historial.sw            =   sw
        historial.save()

        instance.equipo.estado = True
        instance.equipo.save()
        instance.delete()
        return redirect('PersonaViewDetail', instance.persona.id)

class Historial(View):
    template_name   =   'Historial/historial_persona.html'

    def get(self, request, pk):
        persona =   get_object_or_404(Personas, id = pk )
        context =   {
            'equipos'   :   persona.personalequipohistoria_set.all().order_by('-fecha_entrega'),
            'title'     :   'Historial de {0}'.format(persona)
        }
        return render(request, self.template_name, context )

class HistorialEquipo(View):
    template_name   =   'Historial/historial_equipo.html'
    def get(self, request, pk):
        equipo =   get_object_or_404(Equipo, id = pk )
        context =   {
            'equipos'   :   equipo.personalequipohistoria_set.all().order_by('-fecha_entrega'),
            'title'     :   'Historial de {0}'.format(equipo)
        }
        return render(request, self.template_name, context )
