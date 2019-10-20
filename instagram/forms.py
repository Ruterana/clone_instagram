from .models import Image
from django import forms
class NewpostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_caption','profile']
       