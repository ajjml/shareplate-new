from django.contrib import admin
from .models import FoodDonation, NeedyLocation

# ------------------ FoodDonation Admin ------------------
@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'quantity', 'expiry_date', 'status', 'donor', 'created_at')
    list_filter = ('status', 'expiry_date')
    search_fields = ('food_name', 'donor__username')

# ------------------ NeedyLocation Admin ------------------
@admin.register(NeedyLocation)
class NeedyLocationAdmin(admin.ModelAdmin):
    # Display fields in admin list view
    list_display = ('place_name', 'sender_name', 'address', 'phone_number', 'added_by', 'created_at')
    
    # Searchable fields
    search_fields = ('place_name', 'sender_name', 'phone_number', 'added_by__username')

    # Optional: Add filters
    list_filter = ('added_by',)

    # Custom method for 'address' column
    def address(self, obj):
        if obj.latitude and obj.longitude:
            return f"{obj.place_name} ({obj.latitude}, {obj.longitude})"
        return obj.place_name
    address.short_description = 'Address'
