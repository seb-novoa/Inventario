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
                messages.success(request, 'Se agrego la clase', extra_tags='alert alert-success')
                return redirect('ClaseView')

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
        instance = get_object_or_404(Clase, id = pk)
        if form.is_valid():
            instance.clase = form.cleaned_data['clase']
            instance.save()

            messages.success(request, 'La clase ha sido modificada', extra_tags='alert alert-success')
        else:
            clase = get_object_or_404(Clase, clase = form.cleaned_data['clase'])
            messages.error(request, 'La clase {0} ya se encuentra registrada'.format(clase), extra_tags ='alert alert-danger' )

        context['clase_id'] = instance.id
        return redirect('ClaseView')
        #return render(request, self.template_name, context)

class DeleteClase(ClaseView):
    def post(self, request, pk):
        if 'ic-request' in request.POST:
            messages.success(request, 'La clase se elimino', extra_tags = 'alert alert-success')
            instance = get_object_or_404(Clase, id = pk)
            instance.delete()

        return redirect('ClaseView')
