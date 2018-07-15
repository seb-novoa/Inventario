from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

#   Modelo
from Personal.models import Area

#   Formulario
from Personal.Area.forms import AreaForm, AreaFormUpdate

#   Listas de areas
class AreaView(View):
    template_name   =   'Area/area.html'

    def all_area(self):
        return Area.objects.all()

    def context_data(self, title = 'Area', form = AreaForm()):
        return {
            'title'     :   title,
            'form'      :   form,
            'areas'     :   self.all_area()
        }

    def get(self, request):
        constext    =   self.context_data()
        return render(request, self.template_name, constext)

#       Creacion de areas
class CreateArea(AreaView):
    template_name   =   'base_crear.html'

    def get(self, request):
        context =   self.context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        form    =   AreaForm(request.POST)

        if 'btn-cancelar' in request.POST:
            return redirect('AreaView')

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado el area de trabajo', extra_tags='alert alert-success')
            return redirect('AreaView')
        context =   self.context_data(form = form)
        return render(request, self.template_name, context)

#       Editar un area
class UpdateArea(CreateArea):
    def get(self, request, pk):
        area    =   get_object_or_404(Area, pk = pk)
        context    =   self.context_data(form = AreaFormUpdate(instance = area))
        return render(request, self.template_name, context )

    def post(self, request, pk):
        area    =   get_object_or_404(Area, pk = pk)
        form    =   AreaFormUpdate(request.POST or None, instance = area)

        if 'btn-cancelar' in request.POST:
            return redirect('AreaView')

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado el area de trabajo', extra_tags='alert alert-success')
            return redirect('AreaView')
        context =   self.context_data(form = form)
        return render(request, self.template_name, context)

class DeleteArea(View):
    def post(self, request, pk):
        if 'ic-request' in request.POST:
            area = get_object_or_404(Area, pk = pk)
            area.delete()
            messages.success(request, 'El área se ha eliminado', extra_tags='alert alert-success')
        return redirect('AreaView')
