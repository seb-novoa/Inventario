from django import forms

from .validators import value_is_already_exists, value_exists

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
