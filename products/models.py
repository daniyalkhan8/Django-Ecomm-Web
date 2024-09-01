from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.utils import timezone

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
    sales_price = models.DecimalField(max_digits=15, decimal_places=3)
    qty_on_hand = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='product_images/', default='product_images/product_fallback.png')
    images = models.ManyToManyField(ProductImages, related_name='products')
    slug = models.SlugField(default="" , null=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.seller_id.first_name}"

    def _generate_unique_slug(self, slug):
        verify_product = Product.objects.filter(slug=slug).exists()
        if verify_product:
            slug = f"{slug}-{get_random_string(length=6)}"
        return slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug(slugify(self.name))
        return super().save(*args, **kwargs)
