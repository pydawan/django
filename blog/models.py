from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='Título',
        max_length=32,
    )
    text = models.TextField(
        verbose_name='Texto',
        max_length=1024,
        help_text='Campo limitado a 1024 caracteres.',
    )
    published = models.BooleanField(
        verbose_name='Publicar?',
        help_text='Se o campo estiver marcado o texto será publicado imediatamente.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
