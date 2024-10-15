from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

