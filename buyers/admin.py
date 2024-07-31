from django.contrib import admin
from .models import Buyer
from wishlist.models import WishList


class UserWishlistTabularInLine(admin.TabularInline):
    model = WishList


class UserAdmin(admin.ModelAdmin):
    inlines = [UserWishlistTabularInLine]

admin.site.register(Buyer, UserAdmin)
