from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from Personal.models import Personas

from PersonalEquipo.forms import RelacionForm

class Asignar(View):
    template_name   =   'base_crear.html'
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
        form        =   RelacionForm(request.POST)

        if form.is_valid():
            r       =   form.save()
            r.persona   =   persona
            r.save()
            return redirect('PersonaViewDetail', pk)
        context     =   self.context_data(form = form)
        return render(request, self.template_name, context)
