# myapp/models.py
from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def total_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.user.username} - {self.item.name}"
