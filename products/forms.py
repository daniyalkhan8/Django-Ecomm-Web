from django import forms

from .models import Product


class ProductCreatForm(forms.ModelForm):
    featured_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'sales_price', 
            'qty_on_hand', 
            'category',
            'featured_image'
        ]
