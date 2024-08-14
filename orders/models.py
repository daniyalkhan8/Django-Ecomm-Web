from django.db import models

from users.models import CustomUser
from products.models import Product
from utils.models import City, State


class Order(models.Model):
    ORDER_STATES = [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    buyer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=14, decimal_places=3)
    order_status = models.CharField(choices=ORDER_STATES, default='draft')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class OrderItem(models.Model):
    ITEM_STATUS = [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=3)
    order_item_status = models.CharField(choices=ITEM_STATUS, default='draft')
