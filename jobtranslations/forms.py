from django import forms
from .models import Paste

class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ('job_description', 'job_qualifications', 'paster_email',)
