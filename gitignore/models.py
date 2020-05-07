from django.db import models


class Gitignore(models.Model):
    content = models.CharField(
        verbose_name='Conteúdo',
        max_length=2048,
    )
    tag = models.CharField(
        verbose_name='Tag',
        max_length=32,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
