# Generated by Django 3.0.5 on 2020-04-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitignore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitignore',
            name='content',
            field=models.CharField(max_length=2048, verbose_name='Conteúdo'),
        ),
    ]
