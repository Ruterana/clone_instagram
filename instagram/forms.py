from .models import Image,Profile,Comments
from django import forms
class NewpostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_caption','profile','post']
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']      