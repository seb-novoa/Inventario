from django import forms

#   Modelos de Personal.models
from Personal.models import Puesto

#   Formulario para agregar y editar un puesto
class PuestoForm(forms.ModelForm):
    class Meta:
        model   =   Puesto
        fields  =   ('puesto', )
        widgets =   {
            'puesto'    :   forms.fields.TextInput(attrs = {
                'class'    :   'form-control'
            })
        }

    #   Solo valido si no existe un puesto con el mismo nombre
    def clean_puesto(self):
        data    =   self.cleaned_data['puesto']
        if Puesto.objects.filter(puesto = data.lower()).exists():
            raise forms.ValidationError('El puesto ya se encuentra registrado')
        return data
