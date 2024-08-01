from django.contrib import admin
from .models import Cart, CartItem


class CartItemTabularInLine(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemTabularInLine]

admin.site.register(Cart, CartAdmin)
