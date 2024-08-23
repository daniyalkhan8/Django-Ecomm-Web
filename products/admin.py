from django.contrib import admin
from .models import Category, Product
from reviews.models import Review


class ProductReviewsTabularInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductReviewsTabularInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
