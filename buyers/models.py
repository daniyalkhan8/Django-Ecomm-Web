from django.db import models
from utils.models import City, State
from django.contrib.auth.models import User


class Buyer(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=20)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user_id.first_name
    
