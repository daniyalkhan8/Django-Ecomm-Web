from django.db import models
from sellers.models import Seller

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    sales_price = models.DecimalField(max_digits=7, decimal_places=3)
    qty_on_hand = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.seller_id.user_id.first_name}"


class ProductImages(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
