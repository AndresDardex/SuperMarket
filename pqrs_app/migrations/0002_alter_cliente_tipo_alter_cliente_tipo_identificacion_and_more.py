# Generated by Django 4.2.20 on 2025-03-27 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Cliente', 'Cliente'), ('Gestor', 'Gestor')], default='Cliente', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_identificacion',
            field=models.CharField(choices=[('Cédula de Ciudadanía', 'Cédula de Ciudadanía'), ('Tarjeta de Identidad', 'Tarjeta de Identidad'), ('Cédula de Extranjería', 'Cédula de Extranjería'), ('Pasaporte', 'Pasaporte')], max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='validacion',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='pqrs',
            name='tipo_radicado',
            field=models.CharField(choices=[('Petición', 'Petición'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo'), ('Sugerencia', 'Sugerencia')], max_length=25),
        ),
    ]
