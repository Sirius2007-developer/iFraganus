# Generated by Django 5.0.1 on 2024-02-19 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_kurs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='time',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_date',
        ),
        migrations.DeleteModel(
            name='Kurs',
        ),
        migrations.DeleteModel(
            name='Time_lesson',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]
