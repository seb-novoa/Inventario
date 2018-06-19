from django import forms
from django.forms.models import ModelForm

from Personal.models import Puestos, Areas, Personas
from .validators import (
    value_is_already_exists, value_exists, value_is_correct_expression_regular,
    value_area_is_already_exists, value_cdc_is_already_exists,
    value_exists_area
    )

class PuestosInputForm(forms.Form):
    Puesto = forms.CharField( validators = [value_exists])

    def clean_Puesto(self):
        data = self.cleaned_data['Puesto']
        if data is not data.lower():
            data = data.lower()
        return data

class PuestosInputFormEditar(PuestosInputForm):
    Puesto = forms.CharField(validators = [value_is_already_exists])


class PuestosInputFormGuardar(PuestosInputForm):
    Puesto = forms.CharField()


class AreaInputForm(forms.Form):
    CDC = forms.CharField(
        validators = [value_is_correct_expression_regular, value_cdc_is_already_exists],
        widget=forms.TextInput(attrs={'placeholder': 'Centro de costo'}
        ))
    Area = forms.CharField(
        validators = [value_area_is_already_exists],
        widget=forms.TextInput(attrs={'placeholder': 'Area'}
    ))

    def clean_Area(self):
        data = self.cleaned_data['Area']
        if data is not data.lower():
            data = data.lower()
        return data

class AreaInputFormBuscar(forms.Form):
    Buscar = forms.CharField(
        validators = [value_exists_area],
        )

class PersonaInputForm(forms.Form):

    CHOICES_FIELD   =   [
        ('Gestor', 'Gestor'),
        ('AsignarGestor', 'Asignar gestor'),
        ('SinGestor', 'Sin gestor')
    ]

    Nombre = forms.CharField()
    Area = forms.ModelChoiceField(queryset = Areas.objects.all())
    Puesto = forms.ModelChoiceField(queryset = Puestos.objects.all())
    GestorOpcion = forms.ChoiceField(choices = CHOICES_FIELD, widget = forms.RadioSelect())

    # def clean_Nombre(self):
    #     nombre = self.cleaned_data['Nombre'].split()
    #     if len(nombre) < 3:
    #         raise forms.ValidationError('falta un nombre o apellido.')
    #
    #     return self.cleaned_data['Nombre']

    def clean(self):
        nombre = self.cleaned_data['Nombre'].split()
        if len(nombre) < 3:
            raise forms.ValidationError('falta un nombre o apellido.')
        if len(nombre) == 3:
            persona = Personas.objects.filter(Nombre = nombre[0], Apellido = nombre[1], ApellidoMaterno = nombre[2], Area = self.cleaned_data['Area'])
            if persona:
                raise forms.ValidationError('ya existe esta persona en esta área', code = 'Nombre')
        if len(nombre) > 3:
            persona = Personas.objects.filter(Nombre = nombre[0], NombreSecundario = nombre[1], Apellido = nombre[2], ApellidoMaterno = ''.join(nombre[3:]), Area = self.cleaned_data['Area'])
            if persona:
                raise forms.ValidationError('ya existe esta persona en esta área', code = 'Nombre')
        return self.cleaned_data
