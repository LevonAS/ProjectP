# Generated by Django 4.2.5 on 2023-11-01 14:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0032_lessons_created_at_lessons_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Название урока')),
                ('number', models.IntegerField(verbose_name='Номер урока')),
                ('type', models.CharField(choices=[('Online lesson', 'Онлайн-урок'), ('Video lesson', 'Видеоурок')], max_length=13, verbose_name='Тип урока')),
                ('part1', models.CharField(blank=True, default='Цель урока', max_length=150, verbose_name='Название первой части описания урока')),
                ('description_part1', models.TextField(blank=True, verbose_name='Содержание первой части')),
                ('part2', models.CharField(blank=True, default='Чему научится ребенок?', max_length=150, verbose_name='Название второй части описания урока')),
                ('description_part2', models.TextField(blank=True, verbose_name='Содержание второй части')),
                ('part3', models.CharField(blank=True, default='Что нужно для урока?', max_length=150, verbose_name='Название третьей части описания урока')),
                ('description_part3', models.TextField(blank=True, verbose_name='Содержание третьей части')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lessons_img/', verbose_name='Изображение')),
                ('path_to_file', models.FilePathField(blank=True, path='/media/lessons_videos')),
                ('link', models.CharField(blank=True, max_length=150, verbose_name='Ссылка на онлайн-урок')),
                ('lesson_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата онлайн-урока')),
                ('viewed', models.BooleanField(default=False, verbose_name='Просмотрен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удален')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['course', 'number'],
            },
        ),
        migrations.RemoveField(
            model_name='onlinelesson',
            name='course',
        ),
        migrations.RemoveField(
            model_name='onlinelesson',
            name='students',
        ),
        migrations.RemoveField(
            model_name='videolesson',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('ART', 'ИСКУССТВО'), ('DESIGN', 'ДИЗАЙН'), ('SOFT_SKILLS', 'SOFT SKILLS')], default='ART', max_length=11, verbose_name='Категория курса'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='teaser_video',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\perev\\Downloads\\ProjectP\\app\\media\\teaser_video', verbose_name='Тизер-видео'),
        ),
        migrations.DeleteModel(
            name='Lessons',
        ),
        migrations.DeleteModel(
            name='Onlinelesson',
        ),
        migrations.DeleteModel(
            name='Videolesson',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='mainapp.course'),
        ),
    ]
