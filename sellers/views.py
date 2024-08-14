from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from .forms import SellerRegisterForm, SellerLoginForm, SellerProfileUpdateForm
from utils.models import City


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


@login_required(login_url='/seller/login/')
def SellerChangePassword(request):
    if request.method == "POST":
        change_pswd_form = PasswordChangeForm(request.user, request.POST)
        if change_pswd_form.is_valid():
            user = change_pswd_form.save()
            update_session_auth_hash(request, user)
            return redirect('sellers:home')
    else:
        change_pswd_form = PasswordChangeForm(request.user)
    return render(request, 'sellers/change_password.html', {'form': change_pswd_form})


@login_required(login_url='/seller/login/')
def GetCities(request):
    data = json.loads(request.body)
    state_id = data["state_id"]
    cities = City.objects.filter(state_id__id=state_id).order_by("name")
    return JsonResponse(list(cities.values("id", "name")), safe=False)
