# Generated by Django 2.2.2 on 2019-06-21 03:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miexamen', '0006_auto_20190620_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 20, 23, 25, 8, 691268), null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='tipo_examen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='miexamen.ListaExamen'),
        ),
    ]