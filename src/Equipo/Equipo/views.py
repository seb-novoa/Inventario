from django.shortcuts import render, redirect
from django.views import View

from Equipo.Equipo.forms import EquipoCreateForm

# CreateEquipo

class CreateEquipo(View):
    template_name   =   'Equipo/create_equipo_form.html'

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
            form.save()
            return redirect('CreateEquipo')

        context     =   self.context_data(form = form)
        return render(request, self.template_name, context)
