# Generated by Django 2.2.17 on 2020-12-01 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0006_auto_20201117_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 10, 2, 18, 409432, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]