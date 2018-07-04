from django import forms

from PersonalEquipo.models import PersonalEquipo

class RelacionForm(form.ModelForm):
    class Meta:
        model   =   PersonalEquipo
        fields  =   ('persona', 'equipos', 'fecha_termino', )
        
