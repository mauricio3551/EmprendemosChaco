from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)  
    author = models.CharField(max_length=100, default='Desconocido')
    image = models.ImageField(upload_to='items/', null=True, blank=True)  # Nuevo campo para la imagen

    def __str__(self):
        return self.name


