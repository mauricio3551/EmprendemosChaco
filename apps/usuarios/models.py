from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)  
    author = models.CharField(max_length=100, default='Desconocido')

    def __str__(self):
        return self.name    

