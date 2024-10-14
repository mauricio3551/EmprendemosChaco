from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from apps.categoria.models import Categoria

def validar_extension(valor):
	if not valor.name.endswith(settings.ALLOWED_IMG):
		raise ValidationError("Ese formato de imagen no esta permitido.")

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='post/thumbnail', null=True, blank=False, validators=[validar_extension])
    publish_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    category = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.title, self.category, self.user)
    
    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    publish_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=False, on_delete=models.CASCADE, related_name='commentsPost')

    def __str__(self):
       return '%s - %s - %s - %s' % (self.post.title, self.user, self.id , self.content)

