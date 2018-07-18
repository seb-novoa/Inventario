from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

#   Modelo
from Personal.models import Persona

#   Formulario
from Personal.Persona.forms import PersonaForm, UpdatePersonaForm, PersonaGestorForm, PersonaBuscarForm

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


        form    =   PersonaGestorForm(request.POST, instance = persona)


        if form.is_valid():
            persona.persona_set.add(form.cleaned_data['GestorIdentificador'])
            return redirect(persona)
        return render(request, self.template_name, self.context_data(form = form))

class PersonaGestorDelete(View):
    def post(self, request, pk):
        if 'btn-eliminar' in request.POST:
            gestor  =   get_object_or_404(Persona, pk = pk)
            persona =   Persona.objects.get(pk = request.POST.get('btn-eliminar'))
            gestor.persona_set.remove(persona)
        return redirect(gestor)

class PersonaBuscar(View):
    template_name   =   'Persona/persona.html'

    def all_persona(self):
        return Persona.objects.all().order_by('area')

    def context_data(self, form = PersonaBuscarForm()):
        return {
            'title' :   'Personal',
            'form'  :   form
        }

    def get_persona_by_nombre(self, nombre):
        personas = self.all_persona()
        nombre_length = len(nombre.split())
        if nombre_length == 1:
            if personas.filter(nombre__startswith = nombre) or personas.filter(apellido_paterno__startswith=nombre):
                return personas.filter(nombre__startswith = nombre) or personas.filter(apellido_paterno__startswith=nombre)
        elif nombre_length == 2:
            if personas.filter(nombre__startswith = nombre[0]) or personas.filter(apellido_paterno__startswith=nombre[1]):
                return personas.filter(nombre__startswith = nombre[0]) or personas.filter(apellido_paterno__startswith=nombre[1])
        elif nombre_length >= 3:
            if personas.filter(nombre__startswith = nombre[0]) or personas.filter(apellido_paterno__startswith=nombre[1]) or  personas.filter(apellido_materno__startswith=nombre[2]):
                return personas.filter(nombre__startswith = nombre[0]) or personas.filter(apellido_paterno__startswith=nombre[1]) or  personas.filter(apellido_materno__startswith=nombre[2])

    def get_persona_by_nombre_and_area(self, nombre, area ):
        personas    =   self.all_persona()
        nombre_length   =   len(nombre.split())
        if nombre_length == 1:
            if personas.filter(nombre__startswith = nombre, area = area) or personas.filter(apellido_paterno__startswith=nombre, area = area) :
                return personas.filter(nombre__startswith = nombre, area = area ) or personas.filter(apellido_paterno__startswith=nombre, area = area)
        elif nombre_length == 2:
            if personas.filter(nombre__startswith = nombre[0], area = area) or personas.filter(apellido_paterno__startswith=nombre[1], area = area) :
                return personas.filter(nombre__startswith = nombre[0], area = area) or personas.filter(apellido_paterno__startswith=nombre[1], area = area) 
        elif nombre_length >= 3:
            if personas.filter(nombre__startswith = nombre[0], area = area) or personas.filter(apellido_paterno__startswith=nombre[1], area = area) or  personas.filter(apellido_materno__startswith=nombre[2], area = area) :
                return personas.filter(nombre__startswith = nombre[0], area = area) or personas.filter(apellido_paterno__startswith=nombre[1], area = area) or  personas.filter(apellido_materno__startswith=nombre[2], area = area) 


    def get(self, request):
        return render(request, self.template_name, self.context_data())

    def post(self, request):
        form    =   PersonaBuscarForm(request.POST)
        context =   self.context_data(form = form)

        if form.is_valid():
            #   Buscar por nombre y area
            if form.cleaned_data['nombre'] and form.cleaned_data['area']:
                nombre = form.cleaned_data['nombre']
                area   = form.cleaned_data['area']
                obtenido = self.get_persona_by_nombre_and_area(nombre, area)
                context['obtenido'] = obtenido

            #   Buscar solo por Nombre
            if not form.cleaned_data['area']:
                nombre = form.cleaned_data['nombre']
                obtenido = self.get_persona_by_nombre(nombre)

                context['obtenido'] = obtenido

            #   Buscar solo por Area
            if not form.cleaned_data['nombre']:
                area = form.cleaned_data['area']
                obtenido = area.persona_set.all()
                context['personal'] = obtenido
                context['area'] = area
                context['equipos'] = area.persona_set.filter(personalequipo__estado=True).count()
        return render(request, self.template_name, context)
