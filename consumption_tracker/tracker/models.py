from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ice_cream = models.IntegerField(default=0)
    coffee = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(default=timezone.now)


class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ice_cream = models.IntegerField(default=0)
    coffee = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def update_total_price(self):
        ice_cream_price = self.ice_cream * 2.00  # Assume $2 per ice cream
        coffee_price = self.coffee * 1.50        # Assume $1.5 per coffee
        self.total_price = ice_cream_price + coffee_price
        self.save()

    def __str__(self):
        return f"{self.user.username} - Total Price: {self.total_price}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, blank=True)
    preferences = models.TextField(blank=True)

    def __str__(self):
        return self.user.username



