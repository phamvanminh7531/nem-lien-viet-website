# Generated by Django 5.0.4 on 2024-04-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_category_name_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Tên Sản Phẩm'),
        ),
    ]