# Generated by Django 5.0 on 2024-01-19 06:57

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_cart_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='productname', unique=True),
        ),
    ]
