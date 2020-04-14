from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.Textarea(
                attrs={
                    'class': 'textarea',
                },
            ),
        }
