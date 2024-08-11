from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SellerRegisterForm, SellerLoginForm, SellerProfileUpdateForm


def SellerRegister(request):
    if request.method == "POST":
        register_form = SellerRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.user_type = 'seller'
            user.save()
            return redirect('sellers:login')
    else:
        register_form = SellerRegisterForm()
    return render(request, 'sellers/register.html', {'form': register_form})


def SellerLogin(request):
    if request.method == "POST":
        login_form = SellerLoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            seller = authenticate(request, email=email, password=password)
            if seller and seller.user_type == 'seller':
                login(request, seller)
                return redirect('sellers:home')
    else:
        login_form = SellerLoginForm()
    return render(request, 'sellers/login.html', {'form': login_form})


@login_required(login_url='/seller/login/')
def SellerHome(request):
    return render(request, 'sellers/home.html')


@login_required(login_url='/seller/login/')
def SellerLogout(request):
    logout(request)
    return redirect('sellers:login')


@login_required(login_url='/seller/login/')
def SellerUpdateProfile(request):
    if request.method == "POST":
        profile_update_form = SellerProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user
        )
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('sellers:home')
    else:
        profile_update_form = SellerProfileUpdateForm(instance=request.user)
    return render(request, 'sellers/profile.html', {'form': profile_update_form})
