from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView

import re

from Personal.models import Puestos, Areas, Personas
from Personal.forms import(
    PuestosInputForm, PuestosInputFormEditar, PuestosInputFormGuardar,
    AreaInputForm, AreaInputFormBuscar, AreaEditarForm,
    PersonaInputForm, PersonaEditarForm, PersonaBuscarForm,
)

class PuestoView(View):
    def all_puestos(self):
        return Puestos.objects.all()

    def context_contructor(self, title, form):
        context = {
            'title' :   title,
            'form'  :   form
        }
        return context

    def get(self, request, *args, **kwargs):

        form = PuestosInputForm()
        context = self.context_contructor('Puestos de trabajo', form)
        context['puestos'] = self.all_puestos()
        if request.GET.get('ic-request'):
            context['values'] = 'bangindi'
        return render(request, 'Personal/puesto.html', context)

    def post(self, request, *args, **kwargs):
        form = PuestosInputForm()
        context = self.context_contructor('Puestos de trabajo', form)
        if 'btn-guardar' in request.POST:
            form = PuestosInputFormGuardar(request.POST)
            if form.is_valid():
                new_puesto = form.cleaned_data.get('Puesto')
                obj, created = Puestos.objects.get_or_create(Puesto = new_puesto)
                if created:
                    messages.success(request, 'El puesto "{p}" ha sido creado'.format(p = obj.Puesto))
                else:
                    messages.error(request, 'El puesto "{p}" ya se encuentra registrado'.format(p = obj.Puesto))

        if 'btn-editar' in request.POST:
            new_puesto = request.POST.get('btn-editar')
            instance = Puestos.objects.get(id = new_puesto)
            return redirect(instance)

        if 'btn-eliminar' in request.POST:
            del_puesto = request.POST.get('btn-eliminar')
            instance = Puestos.objects.get(id = del_puesto)
            messages.success(request, 'El puesto "{p}" ha sido eliminado.'.format(p = instance))
            instance.delete()
        context['puestos'] = self.all_puestos()
        return render(request, 'Personal/puesto.html', context)

class PuestoViewEditar(View):
    def get(self, request, puesto_id, *args, **kwargs):
        # if request.GET.get('ic-request'):
        #     puesto = get_object_or_404(Puestos, id = puesto_id)
        #     context = {
        #         'formEditar' : PuestosInputForm(instance = puesto),
        #         'value' : 'wawingis',
        #         }
        puesto = Puestos.objects.get(id  = puesto_id)
        form = PuestosInputFormEditar(instance = puesto)
        context = {
            'title': 'Editar puesto "{p}"'.format(p = puesto),
            'form' : form
        }
        context['puesto'] = puesto
        return render(request, 'Personal/puesto-editar.html', context)

    def post(self, request, puesto_id, *args, **kwargs):
        if 'btn-cancelar' in request.POST:
            return redirect('PuestoView')
        form = PuestosInputFormEditar(request.POST)
        puesto = Puestos.objects.get(id  = puesto_id)
        context = {
            'title': 'Editar puesto "{p}"'.format(p = puesto),
            'form' : form
        }

        if form.is_valid():
            new_puesto = form.cleaned_data.get('Puesto')
            obj, created = Puestos.objects.update_or_create(defaults = {'Puesto' : new_puesto},  id= puesto_id)
            if created:
                messages.error(request, 'El puesto no ha sido creado')
            else:
                messages.success(request, 'El puesto se ha guardado')
                return redirect('PuestoView')
        else:
            messages.error(request, 'El puesto ya existe')
            return redirect('PuestoView')
        context['puesto'] = puesto
        return render(request, 'Personal/puesto-editar.html', context)

class AreaView(View):
    def context_contructor(self, title, form):
        context = {
            'title' :   title,
            'form'  :   form
        }
        return context

    def objecto(self, value):
        patron = re.compile('^[A-Z]{4}[0-9]{4}$')
        if patron.match(value.upper()):
            obj = Areas.objects.get(CDC = value)
        else:
            obj = Areas.objects.get(Area = value)

        return obj

    def all_areas(self):
        areas = Areas.objects.all()
        return areas

    def get(self, request, *args, **kwargs):
        context = self.context_contructor('Áreas', AreaInputFormBuscar())
        context['areas'] = self.all_areas()
        return render(request, 'Personal/area.html', context)

    def post(self, request, *args, **kwargs):
        context = self.context_contructor('Áreas', AreaInputFormBuscar())


        # if 'btn-buscar' in request.POST:
        #     form = AreaInputFormBuscar(request.POST)
        #     context = self.context_contructor('Area buscando....', form)
        #     if form.is_valid():
        #         obj = self.objecto(form.cleaned_data.get('Buscar'))
        #         context['obj'] = obj

        if 'btn-editar' in request.POST:
            new_area = request.POST.get('btn-editar')
            instance = Areas.objects.get(id = new_area)
            return redirect(instance)

        if 'btn-eliminar' in request.POST:
            del_area = request.POST.get('btn-eliminar')
            instance = Areas.objects.get(id = del_area)
            messages.success(request, 'El area "{p}" ha sido eliminado.'.format(p = instance))
            instance.delete()

        context['areas'] = self.all_areas()
        return render(request, 'Personal/area.html', context)

class AreaViewEditar(SuccessMessageMixin, UpdateView):
    model = Areas
    fields  =   ('CDC', 'Area', )
    template_name = 'Personal/area-guardar.html'
    success_url = reverse_lazy('AreaView')
    success_message = 'Area guardada'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Área'
        return context

    def post(self, request, *args, **kwargs):
        if 'btn-cancelar' in request.POST:
            return redirect('AreaView')
        return super(AreaViewEditar, self).post(self, request, *args, **kwargs)



# class AreaViewEditar(AreaView):
#     def get(self, request, area_id, *args, **kwargs):
#         instance = Areas.objects.get(id = area_id)
#         form  = AreaEditarForm(instance = instance)
#         context = self.context_contructor('Editar área {i}'.format(i = instance.Area), form)
#         return render(request, 'Personal/area-guardar.html', context)
#
#     def post(self, request, area_id, *args, **kwargs):
#         if 'btn-cancelar' in request.POST:
#             return redirect('AreaView')
#         area = Areas.objects.get(id  = area_id)
#         form = AreaEditarForm(request.POST)
#         context = self.context_contructor('Editar área {i}'.format(i = area), form)
#
#         if form.is_valid():
#             new_area = form.cleaned_data.get('Area')
#             new_cdc = form.cleaned_data.get('CDC')
#             created = area.update( CDC = new_cdc, Area = new_area)
#             # obj, created = Areas.objects.update_or_create(defaults = {'Area' : new_area, 'CDC': new_cdc},  id= area_id)
#             # if created:
#             #     messages.error(request, 'El area no ha sido creado')
#             # else:
#             messages.success(request, 'El area se ha guardado')
#             return redirect('/persona/area/')
#         return render(request, 'Personal/area-guardar.html', context)

class AreaViewGuardar(AreaView):
    template = 'Personal/area-guardar.html'

    def correct_field(self, cdc, area):
        cdc_field = Areas.objects.filter(CDC = cdc) or False
        area_field = Areas.objects.filter(Area = area) or False
        return [cdc_field, area_field]

    def get(self, request, *args, **kwargs):
        context = self.context_contructor('Crear Area', AreaInputForm())
        return render(request, self.template, context)


    def post(self, request, *args, **kwargs):
        if 'btn-cancelar' in request.POST:
            return redirect('AreaView')
        form = AreaInputForm(request.POST)
        context = self.context_contructor('Area', form)
        if form.is_valid():
            new_area = [form.cleaned_data.get('CDC'), form.cleaned_data.get('Area')]
            obj, created = Areas.objects.get_or_create(CDC = new_area[0], Area = new_area[1])

            if created:
                context= self.context_contructor('Area', form)
                messages.success(request, 'El área ha sido creada')
                return redirect('AreaView')
            else:
                context= self.context_contructor('Area', form)
                context['area'] = obj
        else:
            cdc = request.POST.get('CDC')
            area = request.POST.get('Area')
            correct = self.correct_field(cdc, area)
            if correct[0]:
                context['area'] = Areas.objects.get(CDC = cdc)
            elif correct[1]:
                context['area'] = Areas.objects.get(Area = area)

        return render(request, self.template, context)

class PersonaView(View):
    def context_contructor(self, title, form):
        context = {
            'title' :   title,
            'form'  :   form
        }
        return context

    def all(self):
        return Personas.objects.all().order_by('Area')

    def get_persona_by_nombre(self, nombre):
        personas = self.all()
        nombre_length = len(nombre.split())
        if nombre_length == 1:
            if personas.filter(Nombre__startswith = nombre) or personas.filter(Apellido__startswith=nombre) or personas.filter(NombreSecundario__startswith=nombre):
                return personas.filter(Nombre__startswith = nombre) or personas.filter(Apellido__startswith=nombre) or personas.filter(NombreSecundario__startswith=nombre)
        elif nombre_length == 2:
            if personas.filter(Nombre__startswith = nombre[0]) or personas.filter(Apellido__startswith=nombre[1]):
                return personas.filter(Nombre__startswith = nombre[0]) or personas.filter(Apellido__startswith=nombre[1])
            if personas.filter(Nombre__startswith = nombre[0]) or personas.filter(NombreSecundario__startswith=nombre[1]):
                return personas.filter(Nombre__startswith = nombre[0]) or personas.filter(Apellido__startswith=nombre[1])
        elif nombre_length >= 3:
            if personas.filter(Nombre__startswith = nombre[0]) or personas.filter(Apellido__startswith=nombre[1]) or  personas.filter(ApellidoMaterno__startswith=nombre[2]):
                return personas.filter(Nombre__startswith = nombre[0]) or personas.filter(Apellido__startswith=nombre[1]) or  personas.filter(ApellidoMaterno__startswith=nombre[2])
            if personas.filter(Nombre__startswith = nombre[0]) or personas.filter(NombreSecundario__startswith=nombre[1]) or  personas.filter(Apellido__startswith=nombre[2]):
                return personas.filter(Nombre__startswith = nombre[0]) or personas.filter(NombreSecundario__startswith=nombre[1]) or  personas.filter(Apellido__startswith=nombre[2])

    def get_persona_by_nombre_y_area(self, nombre, area):
        personas = self.all()
        nombre_length = len(nombre.split())
        if nombre_length == 1:
            if personas.filter(Nombre__startswith = nombre, Area = area) or personas.filter(Apellido__startswith=nombre, Area = area) or personas.filter(NombreSecundario__startswith=nombre, Area = area):
                return personas.filter(Nombre__startswith = nombre, Area = area) or personas.filter(Apellido__startswith=nombre, Area = area) or personas.filter(NombreSecundario__startswith=nombre, Area = area)
        elif nombre_length == 2:
            if personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(Apellido__startswith=nombre[1], Area = area):
                return personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(Apellido__startswith=nombre[1], Area = area)
            if personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(NombreSecundario__startswith=nombre[1], Area = area):
                return personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(Apellido__startswith=nombre[1], Area = area)
        elif nombre_length >= 3:
            if personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(Apellido__startswith=nombre[1], Area = area) or  personas.filter(ApellidoMaterno__startswith=nombre[2], Area = area):
                return personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(Apellido__startswith=nombre[1], Area = area) or  personas.filter(ApellidoMaterno__startswith=nombre[2], Area = area)
            if personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(NombreSecundario__startswith=nombre[1], Area = area) or  personas.filter(Apellido__startswith=nombre[2], Area = area):
                return personas.filter(Nombre__startswith = nombre[0], Area = area) or personas.filter(NombreSecundario__startswith=nombre[1], Area = area) or  personas.filter(Apellido__startswith=nombre[2], Area = area)

    def get(self, request):
        form = PersonaBuscarForm()
        context =   {
            'form'  :   form,
            'title' :   'Personal'
        }
        return render(request, 'Personal/persona.html', context)
    def post(self, request):
        form = PersonaBuscarForm(request.POST)
        context = self.context_contructor('Buscar Personas', form)
        if form.is_valid():
            if form.cleaned_data['Nombre'] and form.cleaned_data['Area']:
                nombre = form.cleaned_data['Nombre']
                area   = form.cleaned_data['Area']
                obtenido = self.get_persona_by_nombre_y_area(nombre, area)
                print(obtenido)

                context['obtenido'] = obtenido
            if not form.cleaned_data['Area']:
                nombre = form.cleaned_data['Nombre']
                obtenido = self.get_persona_by_nombre(nombre)

                context['obtenido'] = obtenido

            if not form.cleaned_data['Nombre']:
                area = form.cleaned_data['Area']
                obtenido = area.personas_set.all()
                context['personal'] = obtenido
                context['area'] = area



        return render(request, 'Personal/persona.html', context)

class PersonaViewDetail(PersonaView):
    def get(self, request, persona_id):
        persona = get_object_or_404(Personas, id = persona_id)
        context = self.context_contructor('Personal', PersonaBuscarForm())
        context['persona'] = persona
        # if persona.GestorIdentificador:
        #     context['gestor'] = persona.get_gestor_url()


        return render (request, 'Personal/persona-detail.html', context)

class PersonaViewGuardar(PersonaView):
    def get(self, request, *args, **kwargs):
        context = self.context_contructor('Ingresar Persona', PersonaInputForm(initial = {'GestorOpcion': 'SinGestor'}))
        return render(request, 'Personal/persona-guardar.html', context)

    def post(self, request, *args, **kwargs):
        if 'btn-cancelar' in request.POST:
            return redirect('PersonaView')
        form = PersonaInputForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['Nombre']
            area = form.cleaned_data['Area']
            puesto = form.cleaned_data['Puesto']
            created = Personas.objects.create(Nombre = nombre, Area = area, Puesto = puesto)
            messages.success(request, 'La persona ha sido registrada')

            if form.cleaned_data['GestorOpcion'] == 'Gestor':
                created.gestor()
                return redirect(created)

            elif form.cleaned_data['GestorOpcion'] == 'AsignarGestor':
                return redirect(created)

        context = self.context_contructor('Ingresar Persona', form)
        return render(request, 'Personal/persona-guardar.html', context)

class PersonaViewEditar(PersonaView):
    def get(self, request):
        context = {
            'title' :   'Editar Personal',
            'personas' : self.all()
        }
        return render(request, 'Personal/persona-editar.html', context)

    def post(self, request):
        if 'btn-editar' in request.POST:
            persona = get_object_or_404(Personas, id = request.POST['btn-editar'])
            return redirect('PersonaViewEditarGuardar', persona.id)
        if 'btn-eliminar' in request.POST:
            persona = get_object_or_404(Personas, id = request.POST['btn-eliminar'])
            return redirect('PersonaViewEditarDelete', persona.id)
        if 'btn-gestionar' in request.POST:
            persona = get_object_or_404(Personas, id = request.POST['btn-gestionar'])
            return redirect('PersonaViewEditarGestor', persona.id)
        return render(request, 'Personal/persona-editar.html', {'personas' : self.all()})


class PersonaViewEditarGuardar(SuccessMessageMixin, UpdateView):
    model = Personas
    form_class = PersonaEditarForm
    template_name = 'Personal/persona-guardar.html'
    success_url = reverse_lazy('PersonaViewEditar')
    success_message = 'Persona modificada'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']    =   'Editar personal'
        return context

    def post(self, request, *args, **kwargs):
        if 'btn-cancelar' in request.POST:
            return redirect('PersonaViewEditar')
        return super(PersonaViewEditarGuardar, self).post(self, request, *args, **kwargs)


from django.views.generic.edit import DeleteView
class PersonaViewEditarDelete(SuccessMessageMixin, DeleteView):
    model = Personas
    success_url = reverse_lazy('PersonaViewEditar')
    success_message = 'Persona eliminada'
    template_name = 'Personal/persona_confirm_delete.html'



    def get(self, request, pk, *args, **kwargs):
        persona = get_object_or_404(Personas, id = pk)
        gestionados = persona.personas_set.all()
        context = {
            'title' : 'Eliminar persona',
            'persona' : persona,
            'gestionados' : gestionados,
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'btn-cancelar' in request.POST:
            return redirect('PersonaViewEditar')
        return super(PersonaViewEditarDelete, self).post(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PersonaViewEditarDelete, self).delete(request, *args, **kwargs)




# class PersonaViewEditarGuardar(PersonaView):
#     def get(self, request, persona_id, *args, **kwargs):
#         persona = Personas.objects.filter(id = persona_id)
#         form  = PersonaEditarForm(persona)
#         context = self.context_contructor('Editar personal', form)
#         return render(request, 'Personal/persona-guardar.html', context)


class PersonaViewGestor(PersonaView):
    def template(self, persona):
        if persona.Gestor:
            template= 'Personal/persona-gestor.html'
        else:
            template = 'Personal/persona-gestionada.html'
        return template

    def get(self, request, persona_id):
        obj = get_object_or_404(Personas, id = persona_id)
        if obj.Gestor:
            personas = obj.Area.personas_set.all()
            context = {
                'personas':personas,
                'persona_id':int(persona_id),
                'obj' : obj,
            }

            template = self.template(obj)

        else:
            personas = obj.Area.personas_set.filter(Gestor = True)
            context = {
                'personas':personas,
                'persona_id':int(persona_id),
                'obj' : obj,
            }

            template = self.template(obj)
        return render(request, template, context)

    def post(self, request, persona_id):
        obj = get_object_or_404(Personas, id = persona_id)
        messages.success(request, 'Gestion Agregada')
        if obj.Gestor:
            personas = obj.Area.personas_set.all()
            context = {
                'personas':personas,
                'persona_id':int(persona_id),
            }
            ids = request.POST.getlist('choices')
            personas = Personas.objects.filter(id__in = ids).update(GestorIdentificador = obj)
            return redirect('PersonaView')

        else:
            personas = obj.Area.personas_set.filter(Gestor = True)
            context = {
                'personas':personas,
                'persona_id':int(persona_id),
            }
            id = request.POST['choice']
            gestor = get_object_or_404(Personas, id = id)
            obj.GestorIdentificador = gestor
            obj.save()

            return redirect('PersonaView')
        template = self.template(obj)

        return render(request, template, context)

class PersonaViewEditarGestor(PersonaViewGestor):
        def post(self, request, persona_id):
            obj = get_object_or_404(Personas, id = persona_id)
            if obj.Gestor:
                personas = obj.Area.personas_set.all().order_by('-GestorIdentificador')
                context = {
                    'personas':personas,
                    'persona_id':int(persona_id),
                    'obj' : obj,
                }
                ids = request.POST.getlist('choices')
                ids = list(map(int, ids))
                personas_ids = obj.personas_set.all().values('id')

                for i in ids:
                    if i not in [personas_ids[k]['id'] for k in range(0 , len(personas_ids))]:
                         Personas.objects.filter(id = i).update(GestorIdentificador = obj)

                for i in [personas_ids[k]['id'] for k in range(0 , len(personas_ids))]:
                    if i not in ids:
                        Personas.objects.filter(id = i).update(GestorIdentificador = '')

                # personas = Personas.objects.filter(id__in = ids).update(GestorIdentificador = obj)

            else:
                personas = obj.Area.personas_set.filter(Gestor = True)
                context = {
                    'personas':personas,
                    'persona_id':int(persona_id),
                }
                id = request.POST['choice']
                gestor = get_object_or_404(Personas, id = id)
                obj.GestorIdentificador = gestor
                obj.save()
            messages.success(request, 'Gestor modificado')
            template = self.template(obj)
            return render(request, template, context)
