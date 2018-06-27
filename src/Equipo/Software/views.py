from django.shortcuts import render
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
        form = SoftwareCreateForm(request.POST)
        context = self.context_data(form)

        if form.is_valid():
            new_software = form.cleaned_data['software']
            software = Software.objects.create(software = new_software)
            context['form'] = SoftwareCreateForm()
            messages.success(request, 'El software ha sido agregado', extra_tags = 'alert alert-success')

        return render(request, self.template_name, context)
