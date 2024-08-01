from django.db import models


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
