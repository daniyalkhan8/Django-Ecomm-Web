from django import forms

from .models import Product


class ProductCreatForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'sales_price', 
            'qty_on_hand', 
            'category'
        ]
