from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    miniatura = models.ImageField(upload_to='post/miniatura')
    fecha_publicacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.titulo, self.categoria, self.usuario)
    
    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    contenido = models.TextField(max_length=1000)

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=False, on_delete=models.CASCADE, related_name='commentsPost')

    def __str__(self):
       return '%s - %s - %s - %s' % (self.post.titulo, self.usuario, self.id , self.contenido)

