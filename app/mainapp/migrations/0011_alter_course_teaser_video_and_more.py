# Generated by Django 4.2.5 on 2023-10-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_remove_course_category_alter_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teaser_video',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\perev\\Downloads\\ProjectP\\app\\media\\teaser_video', verbose_name='Тизер-видео'),
        ),
        migrations.AlterField(
            model_name='videolesson',
            name='path_to_file',
            field=models.FilePathField(path='/media/lessons_videos'),
        ),
    ]
