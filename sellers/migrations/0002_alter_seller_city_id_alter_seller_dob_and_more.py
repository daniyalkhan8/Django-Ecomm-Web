# Generated by Django 5.0.7 on 2024-08-08 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='city_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.city'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='postal_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='seller',
            name='state_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.state'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
