# Generated by Django 4.2.5 on 2023-11-01 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0041_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 9, 24, 24, 314200, tzinfo=datetime.timezone.utc)),
        ),
    ]
