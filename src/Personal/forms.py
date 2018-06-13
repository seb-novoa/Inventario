from django import forms

from Personal.models import Puestos
from .validators import (
    value_is_already_exists, value_exists, value_is_number,
    value_area_is_already_exists, value_cdc_is_already_exists
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
        validators = [value_is_number, value_cdc_is_already_exists],
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
