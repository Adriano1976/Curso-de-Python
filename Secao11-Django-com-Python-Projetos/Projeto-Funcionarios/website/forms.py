from .models import Funcionario
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONARIOS
# ----------------------------------------------


class InsereFuncionarioForm(forms.ModelForm):
    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label="Biografia",
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campo que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]
