# Generated by Django 3.2.4 on 2023-12-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_supplirs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplirs',
            name='description',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
