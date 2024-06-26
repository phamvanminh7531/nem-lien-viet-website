# Generated by Django 5.0.4 on 2024-04-20 17:11

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_baseinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_name', models.CharField(max_length=250, unique=True, verbose_name='Tên Ảnh')),
                ('images', models.FileField(upload_to=home.models.upload_path, verbose_name='Ảnh')),
            ],
        ),
    ]
