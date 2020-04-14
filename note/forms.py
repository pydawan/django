from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.Textarea(
                attrs={
                    'class': 'textarea',
                },
            ),
        }
