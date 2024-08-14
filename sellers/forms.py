from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser
from utils.models import City


class SellerRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]


class SellerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)


class SellerProfileUpdateForm(UserChangeForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    profile_picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

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

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id__id=state_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.state_id is not None:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
