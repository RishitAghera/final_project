# Generated by Django 3.0.3 on 2020-03-13 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_auto_20200304_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 13, 39, 6, 904428)),
        ),
    ]
