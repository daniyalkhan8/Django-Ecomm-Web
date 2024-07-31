from django.db import models
from buyers.models import Buyer
from products.models import Product


class Cart(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    total_prod_qtys = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=14, decimal_places=3)


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=3)
