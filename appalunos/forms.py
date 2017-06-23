from django import forms
from django.forms import ModelForm, forms

from appAlunos.models import Aluno


class AlunoForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'turno_aula', 'matricula','senha')
