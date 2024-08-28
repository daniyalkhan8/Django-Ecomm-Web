from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, ProductImages
from .forms import ProductCreatForm
from utils.decorators import is_seller


# Seller Products Views

@login_required(login_url="/seller/login/")
@is_seller
def SellerAddProduct(request):
    if request.method == "POST":
        product_form = ProductCreatForm(request.POST)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.seller_id = request.user
            product.save()
            images = request.FILES.getlist('images')
            for image in images:
                product_image = ProductImages.objects.create(image=image)
                product.images.add(product_image)
            return redirect('sellers:home')
    else:
        product_form = ProductCreatForm()
        
    return render(
        request, 
        "products/seller/add_product.html", 
        {"form": product_form}
    )


@login_required(login_url="/seller/login/")
@is_seller
def SellerProductList(request):
    if request.method == "GET":
        product_list = Product.objects.all()[:9]
    return render(
        request, 
        'products/seller/product_list.html', 
        {'product_list': product_list}
    )
