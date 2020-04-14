from django import forms


class AxiosForm(forms.Form):
    first_name = forms.CharField(
        label='Nome',
        max_length=10,
        help_text='Tamanho maximo de 10 caracteres',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    last_name = forms.CharField(
        label='Sobrenome',
        max_length=30,
        help_text='Tamanho maximo de 30 caracteres',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )
