from django.db import models


class Note(models.Model):
    title = models.CharField(
        verbose_name='Título',
        max_length=32,
    )
    text = models.TextField(
        verbose_name='Texto',
        max_length=1024,
        help_text='Campo limitado a 1024 caracteres.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
