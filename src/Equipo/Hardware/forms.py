from django import forms

from Equipo.models import Hardware, Clase

HELP_TEXT_MULTIPLE = 'Manten persionado "Control" para seleccionar mas de uno'

class HardwareCreateForm(forms.ModelForm):
    class Meta:
        model   =   Hardware
        fields  =   ('hardware', 'clases','descripcion',)
        widgets =   {
            'hardware'  :   forms.fields.TextInput(attrs={
                'class' :   'form-control'
            }),

            'descripcion'   :   forms.Textarea(attrs={
                'class' :   'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(HardwareCreateForm, self).__init__(*args, **kwargs)
        self.fields['descripcion'].required = False
        self.fields['clases'].help_text     =   HELP_TEXT_MULTIPLE
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_hardware(self):
        hw = self.cleaned_data['hardware']
        if Hardware.objects.filter(hardware = hw).exists():
            raise forms.ValidationError('El hardware {0} ya se encuentra registrado'.format(self.cleaned_data['hardware']))
        return hw

class HardwareUpdateForm(HardwareCreateForm):
    def clean_hardware(self):
        hw = self.cleaned_data['hardware'].lower()
        if Hardware.objects.filter(hardware = hw).exists():
            i    =    Hardware.objects.get(id = self.instance.id)
            if i.hardware    !=  hw :
                raise forms.ValidationError('El hardware {0} ya se encuentra registrado'.format(self.cleaned_data['hardware']))
        return hw
