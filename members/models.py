from django.db import models
from tinymce.models import HTMLField

from autoslug import AutoSlugField
# Create your models here.

class Members(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    test=models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Employees(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Category(models.Model):
    category_name=models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category_name}"

class Products(models.Model):
    category=models.CharField(max_length=255)
    productname=models.CharField(max_length=255)
    product_perchase_price=models.CharField(max_length=255)
    product_sale_price=models.CharField(max_length=255)
    product_quantity=models.CharField(max_length=255)
    product_status=models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    product_slug=AutoSlugField(populate_from="productname",unique=True,null=True,default=None)
    def __str__(self):
        return f"{self.productname}"

class Suppliers(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)
    contact=models.IntegerField(null=True)
    description=models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Users(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)
    user_slug=AutoSlugField(populate_from="username",unique=True,null=True,default=None)
    def __str__(self):
        return f"{self.username}"


class Cart(models.Model):

    pid=models.CharField(max_length=255)
    productname=models.CharField(max_length=255)
    product_sale_price=models.IntegerField()
    product_quantity=models.IntegerField()
    total_price=models.IntegerField()
    in_stock=models.IntegerField()
    is_deleted = models.BooleanField(default=False)

class Sales(models.Model):

    bid=models.CharField(max_length=255)
    custname=models.CharField(max_length=255)
    custcont=models.CharField(max_length=255)
    sale=models.CharField(max_length=255)
    tamount=models.FloatField()
    disc=models.FloatField()
    netpay=models.FloatField()
    