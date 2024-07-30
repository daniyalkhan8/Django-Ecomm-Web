from django.contrib import admin
from .models import Category, Product, ProductImages


class ProductImagesTabularInline(admin.TabularInline):
    model = ProductImages


class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImagesTabularInline]


admin.site.register(Category)
admin.site.register(Product, ProductsAdmin)
