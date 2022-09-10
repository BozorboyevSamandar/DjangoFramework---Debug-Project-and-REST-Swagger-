from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
