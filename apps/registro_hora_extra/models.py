from django.db import models
from ..funcionarios.models import Funcionarios

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=255)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)


    def __str__(self):
        return "{}".format(self.motivo)