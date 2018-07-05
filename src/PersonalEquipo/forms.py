from django import forms
from django.utils import timezone

from PersonalEquipo.models import PersonalEquipo
from Equipo.models import Equipo

class RelacionForm(forms.ModelForm):
    class Meta:
        model   =   PersonalEquipo
        fields  =   ( 'equipo', 'fecha_termino', )

    def __init__(self, *args, **kwargs):
        super(RelacionForm, self).__init__(*args, **kwargs)
        self.fields['equipo'].queryset   =   Equipo.objects.filter(estado = True)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        if self.cleaned_data['fecha_termino'] <   timezone.now():
            raise forms.ValidationError('Fecha invalida')
        
