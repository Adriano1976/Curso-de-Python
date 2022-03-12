from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    summary = RichTextField(verbose_name='Sumário')
    content = RichTextUploadingField(verbose_name='Conteúdo')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    created_at = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.title
