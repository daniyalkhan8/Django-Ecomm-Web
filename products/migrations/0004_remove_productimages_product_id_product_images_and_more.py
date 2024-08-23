# Generated by Django 5.0.7 on 2024-08-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_category_id_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='products', to='products.productimages'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
