from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from .froms import BuyerRegisterForm, BuyerLoginForm, BuyerProfileUpdateForm
from utils.models import City


def BuyerRegister(request):
    if request.method == "POST":
        register_form = BuyerRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.user_type = 'buyer'
            user.save()
            return redirect('buyers:login')
    else:
        register_form = BuyerRegisterForm()
    return render(request, 'buyers/register.html', {'form': register_form})


def BuyerLogin(request):
    if request.method == "POST":
        login_form = BuyerLoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            buyer = authenticate(request, email=email, password=password)
            if buyer and buyer.user_type == 'buyer':
                login(request, buyer)
                return redirect('buyers:home')
    else:
        login_form = BuyerLoginForm()
    return render(request, 'buyers/login.html', {'form': login_form})


@login_required(login_url='/buyer/login/')
def BuyerHome(request):
    return render(request, 'buyers/home.html')


@login_required(login_url='/buyer/login/')
def BuyerLogout(request):
    logout(request)
    return redirect('buyers:login')


@login_required(login_url='/buyer/login/')
def BuyerUpdateProfile(request):
    if request.method == "POST":
        profile_update_form = BuyerProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user
        )
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('buyers:home')
    else:
        profile_update_form = BuyerProfileUpdateForm(instance=request.user)
    return render(request, 'buyers/profile.html', {'form': profile_update_form})


@login_required(login_url='/buyer/login/')
def BuyerChangePassword(request):
    if request.method == "POST":
        change_pswd_form = PasswordChangeForm(request.user, request.POST)
        if change_pswd_form.is_valid():
            user = change_pswd_form.save()
            update_session_auth_hash(request, user)
            return redirect('buyers:home')
    else:
        change_pswd_form = PasswordChangeForm(request.user)
    return render(request, 'buyers/change_password.html', {'form': change_pswd_form})


@login_required(login_url='/byuer/login/')
def GetCities(request):
    data = json.loads(request.body)
    state_id = data["state_id"]
    cities = City.objects.filter(state_id__id=state_id).order_by("name")
    return JsonResponse(list(cities.values("id", "name")), safe=False)
