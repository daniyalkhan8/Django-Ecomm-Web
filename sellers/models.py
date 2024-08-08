from django.db import models
from utils.models import City, State

from users.models import CustomUser


class Seller(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField(null=True, blank=True)
    city_id = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    street = models.CharField(max_length=50, null=True, blank=True)
    state_id = models.ForeignKey(State, null=True, blank=True, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user_id.first_name
