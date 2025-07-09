from enum import unique
from django.db import models


class Product(models.Model):
    productId = models.CharField(max_length=20, unique=True)
    productCategory = models.CharField(max_length=50)
    productName = models.CharField(max_length=100)
    productColor = models.CharField(max_length=50)
    productImage = models.URLField(max_length=500)
    productSize = models.CharField(max_length=50)
    productQuantity = models.IntegerField()
    productDescription = models.TextField()
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self): 
        return self.productName


class SlideCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Slide(models.Model):
    category = models.ForeignKey(SlideCategory, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category.name}: {self.image_path}"