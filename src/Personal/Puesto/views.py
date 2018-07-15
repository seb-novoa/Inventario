from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

#   Formularios
from Personal.Puesto.forms import PuestoForm

#   Modelo
from Personal.models import Puesto

class PuestoView(View):
    template_name   =   'Puesto/puesto.html'
    def all_puestos(self):
        return Puesto.objects.all()
    def context_data(self, title=    'Puesto de trabajo', form= PuestoForm()):
        return {
            'title'     :   title,
            'form'      :   form,
            'puestos'   :   self.all_puestos()
        }


    def get(self, request):
        context    =   self.context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        form=   PuestoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado el puesto de trabajo', extra_tags='alert alert-success')
            return redirect('PuestoView')
        context=    self.context_data(form = form)
        return render(request, self.template_name, context)

class UpdatePuesto(PuestoView):
    template_name   =   'Puesto/puesto_editar_form.html'

    def get(self, request, pk):
        if not 'ic-request' in request.GET:
            return redirect('PuestoView')

        puesto= get_object_or_404(Puesto, pk = pk)
        context=    self.context_data(form = PuestoForm(instance = puesto))
        context['puesto']   =   puesto
        return render(request, 'Puesto/puesto_editar_form.html', context)

    def post(self, request, pk):
        if 'btn-cancelar' in request.POST:
            return redirect('PuestoView')

        puesto= get_object_or_404(Puesto, pk = pk)
        form=   PuestoForm(request.POST or None, instance = puesto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado el puesto de trabajo', extra_tags='alert alert-success')
        else:
            messages.error(request, 'El puesto ya se encuentra registrado', extra_tags='alert alert-danger')

        return redirect('PuestoView')

class DeletePuesto(PuestoView):
    def post(self, request, pk):
        if 'ic-request' in request.POST:
            puesto = get_object_or_404(Puesto, pk = pk)
            puesto.delete()
            messages.success(request, 'El puesto se ha eliminado', extra_tags='alert alert-success')
        return redirect('PuestoView')
