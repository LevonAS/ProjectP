# Generated by Django 4.2.5 on 2023-10-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_course_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='benefit_img/', verbose_name='Изображение'),
        ),
    ]
