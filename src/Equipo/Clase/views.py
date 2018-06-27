from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from Equipo.models import Clase
from Equipo.Clase.forms import ClaseCreateForm, ClaseUpdateForm

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
        if 'btn-cancelar' in request.POST:
            return redirect('ClaseView')
        form = ClaseCreateForm(request.POST)
        context = self.context_data(form)
        if 'btn-guardar' in request.POST:
            if form.is_valid():
                new_clase = form.cleaned_data['clase']
                clase = Clase.objects.create(clase = new_clase)
                context['form'] = ClaseCreateForm()
                messages.success(request, 'Se agrego la clase')

        return render(request, self.template_name , context)

class UpdateClase(ClaseView):
    template_name = 'Clase/clase_update_form.html'
    def get(self, request, pk):
        instance = get_object_or_404(Clase, id = pk )
        form = ClaseUpdateForm(instance = instance)
        context = self.context_data(form)
        context['clase_id'] = instance.id
        return render(request, self.template_name, context)

    def post(self, request, pk):
        if 'btn-cancelar' in request.POST:
            return redirect('ClaseView')

        form = ClaseUpdateForm(request.POST)
        context = self.context_data(form)
        if form.is_valid():
            instance = get_object_or_404(Clase, id = pk)
            instance.clase = form.cleaned_data['clase']
            instance.save()

            messages.success(request, 'La clase ha sido modificada')
            return redirect('ClaseView')
        return render(request, self.template_name, context)
