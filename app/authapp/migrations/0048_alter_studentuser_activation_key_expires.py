# Generated by Django 4.2.5 on 2023-11-02 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0047_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 18, 34, 45, 570892, tzinfo=datetime.timezone.utc)),
        ),
    ]
