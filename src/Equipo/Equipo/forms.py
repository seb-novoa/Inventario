from django import forms
import re

from Equipo.models import Equipo, MAC, Hardware, Clase

HELP_TEXT_MULTIPLE = 'Manten persionado "Control" para seleccionar mas de uno'

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

class EquipoUpdateForm(EquipoCreateForm):
    def clean_serie(self):
        data    =   self.cleaned_data['serie']

        if Equipo.objects.filter(serie = data.upper()).exists():
            i   =   Equipo.objects.get(id = self.instance.id)
            if data != i.serie:
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

class EquipoHardwareForm(forms.ModelForm):
    class Meta:
        model   =   Equipo
        fields  =   ('hardware', )

    def __init__(self, *args, **kwargs):
        super(EquipoHardwareForm, self).__init__(*args, **kwargs)
        self.fields['hardware'].queryset    =   Hardware.objects.filter(clases = self.instance.clase)
        self.fields['hardware'].help_text   =   HELP_TEXT_MULTIPLE
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EquipoSoftwareForm(forms.ModelForm):
    class Meta:
        model   =   Equipo
        fields  =   ('software', )

    def __init__(self, *args, **kwargs):
        super(EquipoSoftwareForm, self).__init__(*args, **kwargs)
        self.fields['software'].help_text   =   HELP_TEXT_MULTIPLE
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class BuscarEquipoForm(forms.Form):
    serie   =   forms.CharField(required = False, widget   =   forms.TextInput(attrs   =   {'class'    :   'form-control', 'placeholder'   :   'Buscar'}))
    clase   =   forms.ModelChoiceField(queryset = Clase.objects.all(), required = False, widget  =   forms.fields.Select(attrs   =   {'class'    :   'form-control'}))

    def serie_exists(self, data):
        data = data.upper()
        equipo  =   Equipo.objects.all()
        patron  =   re.compile('([0-9A-F]{2}[:-]){5}([0-9A-F]{2})')

        if  equipo.filter(serie = data).exists() or  equipo.filter(serieEnap = data).exists() or  equipo.filter(serieEntel = data).exists() or patron.match(data.upper()):
            return False
        else:
            return True

    def clean(self):
        if not self.cleaned_data['serie'] and not self.cleaned_data['clase']:
            raise forms.ValidationError('Se debe de ingresar una serie o seleccionar una clase')
        if self.cleaned_data['clase'] == None:
            if self.serie_exists(self.cleaned_data['serie']):
                raise forms.ValidationError('El numero de serie no se encutra')
