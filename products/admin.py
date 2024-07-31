from django.contrib import admin
from .models import Category, Product, ProductImages
from reviews.models import Review


class ProductImagesTabularInline(admin.TabularInline):
    model = ProductImages


class ProductReviewsTabularInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesTabularInline, ProductReviewsTabularInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
