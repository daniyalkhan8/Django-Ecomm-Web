from django.db import models
from django.template.defaultfilters import slugify

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product_images/")


class Product(models.Model):
    seller_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    sales_price = models.DecimalField(max_digits=7, decimal_places=3)
    qty_on_hand = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField(ProductImages, related_name='products')
    slug = models.SlugField(default="" ,null=False, unique=True)

    def __str__(self):
        return f"{self.name} - {self.seller_id.user_id.first_name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
