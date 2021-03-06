# Generated by Django 3.0.2 on 2020-03-03 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200302_1256'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0002_auto_20200303_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Gym')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
