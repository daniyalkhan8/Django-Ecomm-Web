from django.db import models
from django.utils import timezone

from users.models import CustomUser
from products.models import Product


class Cart(models.Model):
    buyer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=14, decimal_places=3)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.buyer_id.name} - {self.total_price}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=3)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - {self.price}"
