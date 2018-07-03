from django import forms
import re

from Equipo.models import Equipo, MAC

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

class CreateMacForm(forms.ModelForm):
    class Meta:
        model   =   MAC
        fields  =   ('mac', 'descripcion',  )

    def __init__(self, *args, **kwargs):
        super(CreateMacForm, self).__init__(*args, **kwargs)
        self.fields['descripcion'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_mac(self):
        data    =   self.cleaned_data['mac'].upper()
        patron  =   re.compile('([0-9A-F]{2}[:-]){5}([0-9A-F]{2})')

        if not patron.match(data):
            raise forms.ValidationError('La MAC no es valida')
        if MAC.objects.filter(mac = data).exists():
            raise forms.ValidationError('La MAC ya esta registrada')
        return data

class UpdateMACForm(CreateMacForm):
    def clean_mac(self):
        data    =   self.cleaned_data['mac'].upper()
        patron  =   re.compile('([0-9A-F]{2}[:-]){5}([0-9A-F]{2})')

        if not patron.match(data):
            raise forms.ValidationError('La MAC no es valida')
        if MAC.objects.filter(mac = data).exists():
            i   =   MAC.objects.get(id = self.instance.id)
            if i.mac != data:
                raise forms.ValidationError('La MAC ya esta registrada')
        return data
