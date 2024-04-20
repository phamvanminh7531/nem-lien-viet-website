# Generated by Django 5.0.4 on 2024-04-20 15:59

import django.db.models.deletion
import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, unique=True, verbose_name='Tên Danh Mục')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, unique=True, verbose_name='Tên Sản Phẩm')),
                ('description', models.TextField(verbose_name='Miêu Tả Sản Phẩm')),
                ('price', models.BigIntegerField(blank=True, verbose_name='Giá Chính Thức')),
                ('fix_price', models.BigIntegerField(blank=True, verbose_name='Giá Khuyến Mãi')),
                ('images', models.FileField(upload_to=home.models.upload_path, verbose_name='Ảnh')),
                ('slug', models.SlugField(blank=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.productcategory', verbose_name='Danh Mục Sản Phẩm')),
            ],
        ),
    ]
