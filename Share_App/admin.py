from django.contrib import admin
from .models import FoodDonation, NeedyLocation

@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'quantity', 'expiry_date', 'status', 'donor', 'created_at')
    list_filter = ('status', 'expiry_date')
    search_fields = ('food_name', 'donor__username')

@admin.register(NeedyLocation)
class NeedyLocationAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'sender_name', 'address', 'phone_number', 'created_at')
    search_fields = ('place_name', 'sender_name', 'address')

