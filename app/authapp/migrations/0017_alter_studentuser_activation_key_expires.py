# Generated by Django 4.2.5 on 2023-10-22 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 21, 41, 22, 832948, tzinfo=datetime.timezone.utc)),
        ),
    ]