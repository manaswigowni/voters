from django import forms
from .models import voterinfo

class VoterForm(forms.ModelForm):
    class Meta:
        model = voterinfo
        fields = '__all__'
