# Generated by Django 4.2.5 on 2023-10-27 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_remove_studentuser_is_subscribed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 9, 42, 30, 765135, tzinfo=datetime.timezone.utc)),
        ),
    ]
