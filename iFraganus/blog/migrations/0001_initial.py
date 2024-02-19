# Generated by Django 5.0.1 on 2024-02-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/index')),
                ('name', models.CharField(max_length=150)),
                ('bio', models.TextField()),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
    ]
