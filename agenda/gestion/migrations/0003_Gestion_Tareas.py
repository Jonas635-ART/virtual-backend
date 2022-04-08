# Generated by Django 4.0.3 on 2022-04-08 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_Descripcion_Nulleable'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='etiquetas',
            field=models.ManyToManyField(related_name='tareas', to='gestion.etiqueta'),
        ),
        migrations.AlterModelTable(
            name='tareas',
            table='tareas',
        ),
    ]
