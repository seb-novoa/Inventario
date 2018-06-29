from django import forms

from Equipo.models import Hardware, Clase

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
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_hardware(self):
        hw = self.cleaned_data['hardware']
        if Hardware.objects.filter(hardware = hw).exists():
            raise forms.ValidationError('El hardware {0} ya se encuentra registrado'.format(self.cleaned_data['hardware']))
        return hw    
