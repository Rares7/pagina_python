# Generated by Django 3.2.8 on 2021-11-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='fecha',
            field=models.DateField(blank=True, help_text='Fecha de publicación', null=True),
        ),
    ]