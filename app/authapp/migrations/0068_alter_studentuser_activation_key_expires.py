# Generated by Django 4.2.5 on 2023-11-09 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0067_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 11, 12, 7, 26, 70993, tzinfo=datetime.timezone.utc)),
        ),
    ]
