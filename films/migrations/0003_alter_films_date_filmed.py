# Generated by Django 4.0.1 on 2022-01-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_films_date_filmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='date_filmed',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
