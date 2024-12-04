# Generated by Django 5.1.3 on 2024-12-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_festivalinterprete_fecha_participacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='entradasDisponibles',
            field=models.PositiveIntegerField(default=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interprete',
            name='fotoFondo',
            field=models.ImageField(default=3, upload_to='interpretes/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='festival',
            name='foto',
            field=models.ImageField(upload_to='festivales/'),
        ),
    ]
