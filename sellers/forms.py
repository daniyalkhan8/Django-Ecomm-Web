from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser
from utils.models import City, State


class SellerRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]


class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SellerProfileUpdateForm(UserChangeForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "email", 
            "dob", 
            "city", 
            "street", 
            "state", 
            "postal_code", 
            "profile_picture"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
