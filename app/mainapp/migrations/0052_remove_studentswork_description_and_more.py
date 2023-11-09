# Generated by Django 4.2.5 on 2023-11-09 12:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0051_alter_studentcourse_purchase_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentswork',
            name='description',
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='students_best_pics_files/', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='StudentsHomework',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='homework_files/', verbose_name='Изображение')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='homework_files/', verbose_name='Изображение')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='homework_files/', verbose_name='Изображение')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='homework_files/', verbose_name='Дополнительный файл')),
                ('comment_student', models.TextField(blank=True, verbose_name='Комментарий студента')),
                ('comment_mentor', models.TextField(blank=True, verbose_name='Комментарий ментора')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studenthomework', to='mainapp.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Домашнее задание студента',
            },
        ),
    ]
