# Generated by Django 5.2 on 2025-04-27 00:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='api.product'),
        ),
    ]
