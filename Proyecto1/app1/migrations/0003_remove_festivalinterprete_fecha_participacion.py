# Generated by Django 5.1.3 on 2024-11-14 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_festival_foto_festivalinterprete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festivalinterprete',
            name='fecha_participacion',
        ),
    ]
