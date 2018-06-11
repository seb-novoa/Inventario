from django import forms

from .validators import value_is_lowercase

class PuestosInputForm(forms.Form):
    Puesto = forms.CharField( validators = [value_is_lowercase])

    def clean_Puesto(self):
        data = self.cleaned_data['Puesto']
        if data is not data.lower():
            data = data.lower()
        return data
