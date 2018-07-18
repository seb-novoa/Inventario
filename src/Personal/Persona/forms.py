from django import forms

#   Modelo
from Personal.models import Persona, Area

HELP_TEXT_MULTIPLE = 'Manten persionado "Control" para seleccionar mas de uno'

class PersonaForm(forms.ModelForm):
    class Meta:
        model   =   Persona
        fields  =   ('nombre', 'apellido_paterno', 'apellido_materno', 'area', 'puesto', 'Gestor',)

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        _nombre =   self.cleaned_data['nombre'].strip()
        _apellido_paterno   =   self.cleaned_data['apellido_paterno'].strip()
        _apellido_materno   =   self.cleaned_data['apellido_materno'].strip()
        _area   =   self.cleaned_data['area']

        if Persona.objects.filter(nombre = _nombre, apellido_paterno = _apellido_paterno, apellido_materno = _apellido_materno, area = _area).exists():
            raise forms.ValidationError('La persona ya se encuentra registrada')
        return self.cleaned_data

class UpdatePersonaForm(PersonaForm):
    def clean(self):
        _nombre =   self.cleaned_data['nombre'].strip()
        _apellido_paterno   =   self.cleaned_data['apellido_paterno'].strip()
        _apellido_materno   =   self.cleaned_data['apellido_materno'].strip()
        _area   =   self.cleaned_data['area']

        if Persona.objects.filter(nombre = _nombre, apellido_paterno = _apellido_paterno, apellido_materno = _apellido_materno, area = _area).exists():
            _persona = Persona.objects.get(nombre = _nombre, apellido_paterno = _apellido_paterno, apellido_materno = _apellido_materno, area = _area)
            if _persona != self.instance:
                raise forms.ValidationError('La persona ya se encuentra registrada')
        return self.cleaned_data

class PersonaGestorForm(forms.ModelForm):
    class Meta:
        model   =   Persona
        fields  =   ('GestorIdentificador', )

    def __init__(self, *args, **kwargs):
        super(PersonaGestorForm, self).__init__(*args, **kwargs)
        self.fields['GestorIdentificador'].queryset     =   Persona.objects.filter(area = self.instance.area, Gestor = False)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PersonaBuscarForm(forms.Form):
    nombre = forms.CharField(required = False, widget   =   forms.TextInput(attrs   =   {'class'    :   'form-control', 'placeholder'   :   'Buscar'}))
    area = forms.ModelChoiceField(queryset = Area.objects.all(), required = False, widget  =   forms.fields.Select(attrs   =   {'class'    :   'form-control'}))

    def clean(self):
        if not self.cleaned_data['nombre'] and not self.cleaned_data['area']:
            raise forms.ValidationError('Se debe ingresar el nombres o un area')
