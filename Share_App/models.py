from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# # Needy Location Model
# class NeedyLocation(models.Model):
#     added_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     sender_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     place_name = models.CharField(max_length=150)
#     address = models.TextField(blank=True, null=True)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     photo = models.ImageField(upload_to="needy_photos/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.place_name} ({self.sender_name})"

#     @property
#     def google_maps_link(self):
#         if self.latitude is not None and self.longitude is not None:
#             return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
#         return None

# # from django.db import models
# # from django.contrib.auth.models import User
# # from decimal import Decimal

# class FoodDonation(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Delivered', 'Delivered'),
#     ]

#     donor = models.ForeignKey(User, on_delete=models.CASCADE)
#     donor_phone = models.CharField(max_length=15, blank=True, null=True)

#     food_name = models.CharField(max_length=200)
#     quantity = models.CharField(max_length=100)
#     expiry_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     photo = models.ImageField(upload_to='food_photos/', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.food_name} by {self.donor.username}"


def food_photo_default():
    return 'default_food.png'  # put this image in your media folder

def location_photo_default():
    return 'default_location.png'  # put this image in your media folder

class FoodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    donor_phone = models.CharField(max_length=20, blank=True, null=True)
    food_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50)
    expiry_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=(('Pending','Pending'),('Delivered','Delivered')))
    photo = models.ImageField(upload_to='food_photos/', blank=True, null=True, default=food_photo_default)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food_name

class NeedyLocation(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    place_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='location_photos/', blank=True, null=True, default=location_photo_default)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name
