# Generated by Django 5.0 on 2023-12-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_rename_supplirs_suppliers'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
