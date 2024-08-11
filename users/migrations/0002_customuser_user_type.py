# Generated by Django 5.0.7 on 2024-08-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('seller', 'Seller'), ('buyer', 'Buyer')], null=True),
        ),
    ]