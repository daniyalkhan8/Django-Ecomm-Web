from django.db import models

from users.models import CustomUser
from products.models import Product


class WishList(models.Model):
    buyer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
