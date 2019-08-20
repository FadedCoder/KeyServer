from django import forms
from . import models


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ['name', 'description']


class KeyForm(forms.ModelForm):
    class Meta:
        model = models.Key
        exclude = ['user', 'created_at', 'last_activation', 'last_check']
