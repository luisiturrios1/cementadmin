# Generated by Django 4.1.7 on 2023-05-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementerio', '0023_alter_terreno_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='columna',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
