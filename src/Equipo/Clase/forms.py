from django import forms
from Equipo.models import Clase

class ClaseCreateForm(forms.Form):
    clase = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))

    def clean(self):
        if Clase.objects.filter(clase = self.cleaned_data.get('clase').lower()).exists():
            raise forms.ValidationError('La clase ya se encuentra registrada')
