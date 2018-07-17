from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

#   Modelo
from Personal.models import Persona

#   Formulario
from Personal.Persona.forms import PersonaForm, UpdatePersonaForm, PersonaGestorForm, PersonaGestionadoForm

class PersonaDetail(View):
    template_name   =   'Persona/persona_detail.html'

    def context_data(self, title = 'Persona', persona = None):
        return {
            'title' :   title,
            'persona'   :   persona
        }

    def get(self, request, pk):
        persona =   get_object_or_404(Persona, pk = pk)
        return render(request, self.template_name, self.context_data(persona = persona))

class CreatePersona(View):
    template_name   =   'base_crear.html'

    def context_data(self, title = 'Persona', form = PersonaForm()):
        return {
            'title' :   title,
            'form'  :   form
        }

    def get(self, request):
        return render(request, self.template_name, self.context_data())

    def post(self, request):            #   BOTON CANCELAR
        form    =   PersonaForm(request.POST)
        if form.is_valid():
            persona =   form.save()
            return redirect(persona)
        return render(request, self.template_name, self.context_data(form = form))

class UpdatePersona(CreatePersona):
    def get(self, request, pk):
        persona =   get_object_or_404(Persona, pk = pk)
        form    =  UpdatePersonaForm(instance = persona)
        return render(request, self.template_name, self.context_data(form = form))

    def post(self, request, pk):
        persona =   get_object_or_404(Persona, pk = pk)

        if 'btn-cancelar' in request.POST:
            return redirect(persona)

        form    =   UpdatePersonaForm(request.POST or None, instance = persona)
        if form.is_valid():
            form.save()
            return redirect(persona)
        return redirect(request, self.template_name, self.context_data(form = form))

class PersonaGestor(View):
    template_name   =   'base_crear.html'

    def context_data(self, title = 'Gestion', form  = None):
        return {
            'title' :   title,
            'form'    :   form
        }

    def get(self, request, pk):
        persona =   get_object_or_404(Persona, pk = pk)
        if persona.Gestor:
            form    =   PersonaGestorForm(instance = persona)
        else:
            form    =   PersonaGestionadoForm(instance = persona)

        return render(request, self.template_name, self.context_data(form = form))

    def post(self, request, pk):
        persona =   get_object_or_404(Persona, pk = pk)

        if 'btn-cancelar' in request.POST:
            return redirect(persona)

        if persona.Gestor:
            form    =   PersonaGestorForm(request.POST, instance = persona)
        else:
            form    =   PersonaGestionadoForm(request.POST, instance = persona)

        if form.is_valid():
            pass
            # form.save()
            # return redirect(persona)
        return render(request, self.template_name, self.context_data(form = form))
