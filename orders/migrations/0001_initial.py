# Generated by Django 5.0.7 on 2024-07-31 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyers', '0001_initial'),
        ('products', '0001_initial'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=3, max_digits=14)),
                ('order_status', models.CharField(choices=[('draft', 'Draft'), ('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyers.buyer')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.city')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.state')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=14)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]