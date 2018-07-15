from django import forms
import re

from Personal.models import Area

class AreaForm(forms.ModelForm):
    patron  =   re.compile('^[A-Z]{4}[0-9]{4}$')
    class Meta:
        model   =   Area
        fields  =   ('cdc', 'area',)
        widgets =   {
            'cdc'   :   forms.fields.TextInput(attrs={
                'class' :   'form-control'
            }),
            'area'   :   forms.fields.TextInput(attrs={
                'class' :   'form-control'
            })
        }

    def clean_cdc(self):
        data    =   self.cleaned_data['cdc'].upper()
        patron  =   self.patron

        if not patron.match(data):
            raise forms.ValidationError('El centro de costo no es valido. Debe de contener cuatro letras seguido de cuatro números')
        if Area.objects.filter(cdc = data).exists():
            raise forms.ValidationError('El centro de costo ya se encuentra registrado')
        return data

    def clean_area(self):
        data    =   self.cleaned_data['area'].lower()
        if Area.objects.filter(area = data).exists():
            raise forms.ValidationError('El area ya se encuentra registrada')
        return data

class AreaFormUpdate(AreaForm):
    def clean_cdc(self):
        data    =   self.cleaned_data['cdc'].upper()
        patron  =   self.patron

        if not patron.match(data):
            raise forms.ValidationError('El centro de costo no es valido. Debe de contener cuatro letras seguido de cuatro números')
        if Area.objects.filter(cdc = data).exists():
            area    =   Area.objects.get(cdc = data)
            if  area != self.instance:
                raise forms.ValidationError('El centro de costo ya se encuentra registrado')
        return data

    def clean_area(self):
        data    =   self.cleaned_data['area'].lower()
        if Area.objects.filter(area = data).exists():
            area    =   Area.objects.get(area = data)
            if area !=  self.instance:
                raise forms.ValidationError('El area ya se encuentra registrada')
        return data
