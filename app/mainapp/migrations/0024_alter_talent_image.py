# Generated by Django 4.2.5 on 2023-10-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_alter_course_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='talent_img/', verbose_name='Изображение'),
        ),
    ]