# Generated by Django 2.2.3 on 2021-09-29 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210924_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(default=datetime.date(2021, 9, 30)),
        ),
    ]