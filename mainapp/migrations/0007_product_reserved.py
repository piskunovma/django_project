# Generated by Django 2.2.17 on 2020-11-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_product_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="reserved",
            field=models.PositiveIntegerField(default=0, verbose_name="зарезервировано"),
        ),
    ]
