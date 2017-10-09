from django import forms

from .models import complain

class Postcomplain(forms.ModelForm):

    class Meta:
        model = complain
        fields = ('location', 'specific_location','details',)