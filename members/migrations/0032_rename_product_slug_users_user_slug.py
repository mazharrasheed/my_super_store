# Generated by Django 5.0 on 2024-01-19 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0031_users_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='product_slug',
            new_name='user_slug',
        ),
    ]
