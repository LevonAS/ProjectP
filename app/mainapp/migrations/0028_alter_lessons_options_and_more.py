# Generated by Django 4.2.5 on 2023-10-29 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_alter_lessons_part1_alter_lessons_part2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ['сourses', 'number'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.RenameField(
            model_name='lessons',
            old_name='part1_description',
            new_name='description_part1',
        ),
        migrations.RenameField(
            model_name='lessons',
            old_name='part2_description',
            new_name='description_part2',
        ),
        migrations.RenameField(
            model_name='lessons',
            old_name='part3_description',
            new_name='description_part3',
        ),
        migrations.RenameField(
            model_name='lessons',
            old_name='part4_description',
            new_name='description_part4',
        ),
        migrations.RenameField(
            model_name='lessons',
            old_name='part5_description',
            new_name='description_part5',
        ),
    ]
