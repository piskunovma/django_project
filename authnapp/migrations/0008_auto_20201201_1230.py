# Generated by Django 2.2.17 on 2020-12-01 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0007_auto_20201201_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 12, 30, 24, 296940, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
