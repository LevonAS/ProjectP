# Generated by Django 4.2.5 on 2023-11-17 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0073_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 19, 8, 52, 1, 915650, tzinfo=datetime.timezone.utc)),
        ),
    ]