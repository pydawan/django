import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.validators import FileExtensionValidator
from django.db import models

location = os.path.join(settings.MEDIA_ROOT, 'documents')
fs = FileSystemStorage(location=location)


class UploadFile(models.Model):
    file = models.FileField(
        storage=fs,
        verbose_name='Selecionar arquivo...',
        help_text='Formato válido <b>*.txt.</b>',
        validators=[FileExtensionValidator(allowed_extensions=['txt'])],
    )
