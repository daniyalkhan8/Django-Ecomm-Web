from django.urls import path
from . import views


app_name = "buyers"
urlpatterns = [
    path("register/", views.BuyerRegister, name="register"),
    path("login/", views.BuyerLogin, name="login"),
    path("", views.BuyerHome, name="home"),
    path("logout/", views.BuyerLogout, name="logout"),
    path("update-profile/", views.BuyerUpdateProfile, name="update_profile"),
    path("change-password/", views.BuyerChangePassword, name="change_password"),
    path("get-cities/", views.GetCities, name='get-cities'),
]
