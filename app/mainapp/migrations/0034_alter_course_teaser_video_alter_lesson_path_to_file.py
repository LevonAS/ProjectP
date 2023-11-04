# Generated by Django 4.2.5 on 2023-11-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_lesson_remove_onlinelesson_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teaser_video',
            field=models.FilePathField(blank=True, null=True, path='/home/teamwork/0111/ProjectP/app/media/teaser_video', verbose_name='Тизер-видео'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='path_to_file',
            field=models.FilePathField(blank=True, path='/home/teamwork/0111/ProjectP/app/media/lessons_videos'),
        ),
    ]
