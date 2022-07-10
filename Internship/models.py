from django.db import models

# Create your models here.

class category(models.Model):
    categoryname = models.CharField(max_length=50)

class products(models.Model):
    categoryname = models.ForeignKey(category, blank=True, null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=100)