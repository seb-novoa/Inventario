from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from Equipo.models import Software
from Equipo.Software.forms import SoftwareCreateForm

class SoftwareView(View):
    template_name = 'Software\software.html'

    def all_programas(self):
        return Software.objects.all()

    def context_data(self, form):
        context = {
            'form'  : form,
            'programas' :   self.all_programas(),
        }
        return context

    def get(self, request):
        context = self.context_data(SoftwareCreateForm())
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)
        form = SoftwareCreateForm(request.POST)
        context = self.context_data(form)

        if form.is_valid():
            new_software = form.cleaned_data['software']
            software = Software.objects.create(software = new_software)
            context['form'] = SoftwareCreateForm()
            messages.success(request, 'El software ha sido agregado', extra_tags = 'alert alert-success')
            return redirect('SoftwareView')
        return render(request, self.template_name, context)

class UpdateSoftware(SoftwareView):
    template_name = 'Software/software_update_form.html'

    def get(self, request, pk):
        instance    =   get_object_or_404(Software, id = pk)
        form        =   SoftwareCreateForm(instance = instance)

        context     =   self.context_data(form)
        context['sw_id']    =   instance.id
        return render(request, self.template_name, context)

    def post(self, request, pk):
        if 'btn-cancelar' in request.POST:
            return redirect('SoftwareView')

        form    =   SoftwareCreateForm(request.POST)
        context =   self.context_data(form)
        instance=   get_object_or_404(Software, id = pk)

        if form.is_valid():
            instance.software   =   form.cleaned_data['software']
            instance.save()
            messages.success(request, 'El software ha sido modificada', extra_tags='alert alert-success')

        else:
            programa = get_object_or_404(Software, software = form.cleaned_data['software'].lower())
            messages.error(request, 'El software {0} ya se encuentra registrado'.format(programa), extra_tags='alert alert-danger')

        return redirect('SoftwareView')

class DeleteSoftware(SoftwareView):
    def post(self, request, pk):
        if 'ic-request' in request.POST:
            instance    =   get_object_or_404(Software, id = pk)
            instance.delete()
            messages.success(request, 'Se elimino el software', extra_tags = 'alert alert-danger')

        return redirect('SoftwareView')
