from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=200)
    email = models.CharField("e-mail", max_length=200)
    matricula = models.CharField("Matrincula", max_length=14, unique=True)

    def __str__(self):
        return self.nome


