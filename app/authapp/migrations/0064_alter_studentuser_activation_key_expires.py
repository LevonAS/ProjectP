# Generated by Django 4.2.5 on 2023-11-07 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0063_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 18, 14, 39, 259802, tzinfo=datetime.timezone.utc)),
        ),
    ]
