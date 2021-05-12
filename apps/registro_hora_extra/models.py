from django.db import models

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.motivo)