# Generated by Django 2.2.14 on 2020-10-04 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora',
            field=models.TimeField(default=datetime.date(2020, 10, 4), verbose_name='Hora'),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
    ]