from django.db import models
from ..funcionarios.models import Funcionarios

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.descricao)
