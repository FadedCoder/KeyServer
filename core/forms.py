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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(KeyForm, self).__init__(*args, **kwargs)
        self.fields['app'].queryset = models.Application.objects.filter(user=self.user)
