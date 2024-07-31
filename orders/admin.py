from django.contrib import admin
from .models import Order, OrderItem


class OrderItemTabularInLine(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInLine]

admin.site.register(Order, OrderAdmin)
