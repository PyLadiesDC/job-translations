from django import forms
from .models import PasteJobURL

class JobURLForm(forms.ModelForm):
    class Meta:
        model = PasteJobURL
        fields = ('job_URL', 'email',)
