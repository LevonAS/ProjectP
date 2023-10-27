# Generated by Django 4.2.5 on 2023-10-27 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_course_preparation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preparation',
            options={'verbose_name': 'Уровень подготовки', 'verbose_name_plural': 'Уровни подготовки'},
        ),
        migrations.AlterField(
            model_name='course',
            name='age_group',
            field=models.CharField(blank=True, max_length=25, verbose_name='Возрастная группа'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(blank=True, max_length=25, verbose_name='Продолжительность курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='lesson_qty',
            field=models.CharField(blank=True, max_length=25, verbose_name='Количество уроков'),
        ),
        migrations.AlterField(
            model_name='course',
            name='preparation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.preparation'),
        ),
    ]
