# Generated by Django 5.0 on 2023-12-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_products_product_quantity_products_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=255)),
                ('productname', models.CharField(max_length=255)),
                ('product_sale_price', models.CharField(max_length=255)),
                ('product_quantity', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]