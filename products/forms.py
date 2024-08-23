from django import forms

from .models import Product, ProductImages


class ProductImagesCreateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = ProductImages
        fields = ['image']


class ProductCreatForm(forms.ModelForm):
    images = forms.ModelMultipleChoiceField(
        queryset=ProductImages.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'sales_price', 
            'qty_on_hand', 
            'category', 
            'images'
        ]
