from django import forms

from Equipo.models import Software

class SoftwareCreateForm(forms.ModelForm):
    class Meta:
        model   =   Software
        fields  =   ('software', )
        widgets =   {
            'software'  :   forms.fields.TextInput(attrs = {
                'class' :   'form-control'
            })
        }

    def clean(self):
        if Software.objects.filter(software = self.cleaned_data['software'].lower()).exists():
            raise forms.ValidationError('El software ya se encuentra registrado.')
