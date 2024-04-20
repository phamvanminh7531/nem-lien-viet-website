# Generated by Django 5.0.4 on 2024-04-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num_1', models.CharField(blank=True, max_length=12, verbose_name='Số Điện Thoại 1')),
                ('phone_num_2', models.CharField(blank=True, max_length=12, verbose_name='Số Điện Thoại 2')),
                ('address', models.CharField(max_length=255, unique=True, verbose_name='Địa Chỉ')),
            ],
        ),
    ]