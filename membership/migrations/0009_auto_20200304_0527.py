# Generated by Django 3.0.2 on 2020-03-04 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20200304_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 4, 5, 26, 58, 510452)),
        ),
    ]
