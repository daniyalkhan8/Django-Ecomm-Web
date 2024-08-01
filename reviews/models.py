from django.db import models
from buyers.models import Buyer
from products.models import Product


class Review(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(blank=True)
    message = models.TextField(max_length=150)
    