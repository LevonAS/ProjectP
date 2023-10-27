# Generated by Django 4.2.5 on 2023-10-27 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0019_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='is_subscribed',
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 9, 38, 53, 357211, tzinfo=datetime.timezone.utc)),
        ),
    ]
