# Generated by Django 4.2.5 on 2023-10-19 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 21, 19, 26, 31, 275883, tzinfo=datetime.timezone.utc)),
        ),
    ]