# Generated by Django 4.2.5 on 2023-10-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_course_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tools',
            field=models.TextField(blank=True, verbose_name='НЕобходимые материалы и инструменты для курса'),
        ),
    ]
