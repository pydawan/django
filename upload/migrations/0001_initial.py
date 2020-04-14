# Generated by Django 3.0.5 on 2020-04-14 14:36

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='Formato válido <b>*.txt.</b>', storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Natorsc\\PycharmProjects\\aula\\media\\documents'), upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])], verbose_name='Selecionar arquivo...')),
            ],
        ),
    ]
