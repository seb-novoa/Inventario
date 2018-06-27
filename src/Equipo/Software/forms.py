from django import forms

class SoftwareCreateForm(forms.Form):
    software = forms.CharField()
