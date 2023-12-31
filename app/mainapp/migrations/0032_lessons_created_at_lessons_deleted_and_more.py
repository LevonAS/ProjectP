# Generated by Django 4.2.5 on 2023-11-01 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_alter_lessons_part3'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessons',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
    ]
