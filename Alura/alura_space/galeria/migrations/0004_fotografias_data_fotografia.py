# Generated by Django 5.0.1 on 2024-01-22 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografias_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografias',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
