# Generated by Django 5.0.7 on 2024-08-14 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='cart',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
