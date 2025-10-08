from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Food Donation Model
class FoodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    expiry_date = models.DateField()
    
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} ({self.quantity}) - {self.status}"

    @property
    def google_maps_link(self):
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        return None


# Needy Location Model
class NeedyLocation(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    place_name = models.CharField(max_length=150)
    address = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    photo = models.ImageField(upload_to="needy_photos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.place_name} ({self.sender_name})"

    @property
    def google_maps_link(self):
        if self.latitude is not None and self.longitude is not None:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        return None

