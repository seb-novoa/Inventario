from django.shortcuts import render
from django.views import View
from django.contrib import messages

from Equipo.models import Clase
from Equipo.Clase.forms import ClaseCreateForm

class ClaseView(View):
    template_name =  'Clase/clase.html'

    def all_clases(self):
        return Clase.objects.all()

    def context_data(self, form):
        context = {
            'form'      :   form,
            'clases'    :   self.all_clases(),
        }
        return context

    def get(self, request):
        form = ClaseCreateForm()
        context = self.context_data(form)
        return render(request, self.template_name , context)

    def post(self, request):
        form = ClaseCreateForm(request.POST)
        context = self.context_data(form)
        if form.is_valid():
            new_clase = form.cleaned_data['clase']
            clase = Clase.objects.create(clase = new_clase)
            context['form'] = ClaseCreateForm()
            messages.success(request, 'Se agrego la clase')
        else:
            context['fc'] = 'form-control-danger'

        return render(request, self.template_name , context)
