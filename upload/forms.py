from django import forms
from django.forms import ModelForm

from .models import UploadFile


class UploadFileForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'
        widgets = {
            'file': forms.FileInput(
                attrs={
                    'accept': '.txt',
                    'class': 'file-input',
                },
            )
        }


class UploadFilesForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'
        widgets = {
            'file': forms.ClearableFileInput(
                attrs={
                    'accept': '.txt',
                    'class': 'file-input',
                    'multiple': True,
                }
            )
        }
