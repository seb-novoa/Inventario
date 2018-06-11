from django.shortcuts import render
from django.views import View

from Personal.models import Puestos
from Personal.forms import PuestosInputForm

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
        print(request.POST)
        if form.is_valid():
            new_puesto = form.cleaned_data.get('Puesto')
            if 'btn-guardar' in request.POST:
                obj, created = Puestos.objects.get_or_create(Puesto = new_puesto)
                if created:
                    context['title']= 'El puesto ha sido creado'
                else:
                    context['title']= 'El puesto "{i}" ya estaba registrado'.format(i = obj.Puesto)

            if 'btn-editar' in request.POST:
                instance = Puestos.objects.filter(Puesto = new_puesto)
                context['form'] = PuestosInputForm()
                return render(request, 'Personal/editar-puesto.html', context)
        return render(request, 'Personal/puesto.html', context)
