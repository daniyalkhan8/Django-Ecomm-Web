from django.urls import path, include
from . import views


app_name = "sellers"
urlpatterns = [
    path("register/", views.SellerRegister, name="register"),
    path("login/", views.SellerLogin, name="login"),
    path("", views.SellerHome, name="home"),
    path("logout/", views.SellerLogout, name="logout"),
    path("update-profile/", views.SellerUpdateProfile, name="update_profile"),
    path("change-password/", views.SellerChangePassword, name="change_password"),
    path("get-cities/", views.GetCities, name='get-cities'),
    path('product/', include('products.urls.seller_urls', namespace='product_seller')),
]
