# Generated by Django 4.2.5 on 2023-11-02 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_delete_advantage_and_more'),
        ('authapp', '0050_alter_studentuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 19, 27, 29, 179679, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='mainapp.course', verbose_name='Курсы'),
        ),
    ]
