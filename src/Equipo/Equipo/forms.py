from django import forms

from Equipo.models import Equipo

class EquipoCreateForm(forms.ModelForm):
    class Meta:
        model   =   Equipo
        fields  =   ('serie', 'serieEntel', 'serieEnap', 'clase')


    def __init__(self, *args, **kwargs):
        super(EquipoCreateForm, self).__init__(*args, **kwargs)
        self.fields['serieEntel'].required = False
        self.fields['serieEnap'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_serie(self):
        data    =   self.cleaned_data['serie']

        if Equipo.objects.filter(serie = data.upper()).exists():
            raise forms.ValidationError('La serie ya se encuentra registrada')
        return data

    def clean_serieEntel(self):
        data    =   self.cleaned_data.get('serieEntel')
        if self.cleaned_data.get('serieEntel'):
            data    =   self.cleaned_data['serieEntel']

            if Equipo.objects.filter(serieEntel = data.upper()).exists():
                raise forms.ValidationError('La serie ya se encuentra registrada')
        return data

    def clean_serieEnap(self):
        data    =   self.cleaned_data.get('serieEnap')
        if self.cleaned_data.get('serieEnap'):
            data    =   self.cleaned_data['serieEnap']

            if Equipo.objects.filter(serieEnap = data.upper()).exists():
                raise forms.ValidationError('La serie ya se encuentra registrada')
        return data
