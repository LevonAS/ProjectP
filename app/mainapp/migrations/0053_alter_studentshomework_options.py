# Generated by Django 4.2.5 on 2023-11-09 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0052_remove_studentswork_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentshomework',
            options={'verbose_name': 'Домашнее задание студента', 'verbose_name_plural': 'Домашние задания студентов'},
        ),
    ]