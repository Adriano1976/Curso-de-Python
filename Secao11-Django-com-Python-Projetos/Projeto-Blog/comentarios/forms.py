from django.core.validators import validate_email
from django.forms.widgets import TextInput, EmailInput, Textarea
from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # Para tirar : depois do nome

    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        if not recaptcha_response:
            self.add_error(
                'comentario',
                'Por favor, marque a caixa "Não sou um robô".'
            )

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdTwbQeAAAAAFNQ_S-bCUAwSrTECkxpaEx7WnPi',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        print(recaptcha_result)
        print(recaptcha_result.get('success'))

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe Mr. Robot, ocorreu um erro.'
            )

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
        widgets = {
            'nome_comentario': TextInput(attrs={
                'placeholder': 'Digite seu nome',
                'class': 'form-control',
            }),
            'email_comentario': EmailInput(attrs={
                'placeholder': 'Digite seu e-mail',
                'class': 'form-control',
            }),
            'comentario': Textarea(attrs={
                'placeholder': 'Digite seu comenário',
                'class': 'form-control',
            }),
        }

# class FormComentario(ModelForm):
#     def clean(self):
#         data = self.cleaned_data
#         nome = data.get('nome_comentario')
#         email = data.get('email_comentario')
#         comentario = data.get('comentario')
#
#         if len(nome) < 5:
#             self.add_error(
#                 'nome_comentario',
#                 'Nome precisa ter mais de 5 caracteres.'
#             )
#
#     class Meta:
#         model = Comentario
#         fields = ('nome_comentario', 'email_comentario', 'comentario')
