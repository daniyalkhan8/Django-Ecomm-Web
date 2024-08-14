from django.db import models

from users.models import CustomUser
from products.models import Product


class Review(models.Model):
    buyer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(blank=True)
    message = models.TextField(max_length=150)
    