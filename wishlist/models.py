from django.db import models
from buyers.models import Buyer
from products.models import Product


class WishList(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
