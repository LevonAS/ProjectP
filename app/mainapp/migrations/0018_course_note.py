# Generated by Django 4.2.5 on 2023-10-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_course_teaser_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='note',
            field=models.CharField(default='', max_length=200, verbose_name='Цель курса'),
        ),
    ]