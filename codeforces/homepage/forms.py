from django import forms

class HandleForm(forms.ModelForm):
    class Meta:
        fields = ['handle']