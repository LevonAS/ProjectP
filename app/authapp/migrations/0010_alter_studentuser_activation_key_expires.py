# Generated by Django 4.2.5 on 2023-10-15 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 9, 48, 55, 432753, tzinfo=datetime.timezone.utc)),
        ),
    ]