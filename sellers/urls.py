from django.urls import path
from . import views


app_name = "sellers"
urlpatterns = [
    path("register/", views.SellerRegister, name="register"),
    path("login/", views.SellerLogin, name="login"),
    path("home/", views.SellerHome, name="home"),
    path("logout/", views.SellerLogout, name="logout"),
    path("update_profile/", views.SellerUpdateProfile, name="update_profile"),
    path("get-cities/", views.GetCities, name='get-cities'),
]
