# Generated by Django 5.0.4 on 2024-04-20 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_name',
            new_name='category',
        ),
    ]