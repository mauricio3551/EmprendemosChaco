from django.db import models

from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    es_superuser = models.BooleanField(default = False)
    es_colaborador = models.BooleanField(default = False)
    es_miembro = models.BooleanField(default = True)

