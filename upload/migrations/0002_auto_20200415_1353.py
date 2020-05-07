# Generated by Django 3.0.5 on 2020-04-15 13:53

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(help_text='Formato válido <b>*.txt.</b>', storage=django.core.files.storage.FileSystemStorage(location='/home/natorsc/Projetos/django-master/media/documents'), upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])], verbose_name='Selecionar arquivo...'),
        ),
    ]