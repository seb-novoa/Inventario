from django import forms

from PersonalEquipo.models import PersonalEquipo

class RelacionForm(forms.ModelForm):
    class Meta:
        model   =   PersonalEquipo
        fields  =   ( 'equipo', 'fecha_termino', )
