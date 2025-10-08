from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from .models import FoodDonation, NeedyLocation

# ------------------ Pages ------------------
def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

# ------------------ Auth ------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        return redirect('dashboard')

    return render(request, 'register.html')

# ------------------ Dashboard ------------------
@login_required
def dashboard(request):
    food_items = FoodDonation.objects.filter(status="Pending").order_by("-created_at")
    needy_locations = NeedyLocation.objects.all().order_by("-created_at")
    return render(request, "dashboard.html", {
        "food_items": food_items,
        "needy_locations": needy_locations,
    })

# ------------------ Food Donation ------------------
@login_required
def share_food_view(request):
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        quantity = request.POST.get("quantity")
        expiry_date = request.POST.get("expiry_date")
        status = request.POST.get("status")

        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        FoodDonation.objects.create(
            donor=request.user,
            food_name=food_name,
            quantity=quantity,
            expiry_date=expiry_date,
            status=status,
            latitude=float(latitude) if latitude not in [None, ''] else None,
            longitude=float(longitude) if longitude not in [None, ''] else None,
        )
        return redirect("dashboard")

    return render(request, "sharefood.html")

@login_required
def delete_food(request, pk):
    food = get_object_or_404(FoodDonation, pk=pk, donor=request.user)
    if request.method == "POST":
        food.delete()
    return redirect("dashboard")

# ------------------ Needy Locations ------------------
@login_required
def share_location(request):
    if request.method == "POST":
        sender_name = request.POST.get("sender_name")
        phone_number = request.POST.get("phone_number")
        place_name = request.POST.get("place_name")
        photo = request.FILES.get("photo")
        lat = request.POST.get("latitude")
        lon = request.POST.get("longitude")

        try:
            latitude = Decimal(lat) if lat not in [None, ''] else None
            longitude = Decimal(lon) if lon not in [None, ''] else None
        except InvalidOperation:
            latitude = None
            longitude = None

        NeedyLocation.objects.create(
            added_by=request.user,
            sender_name=sender_name,
            phone_number=phone_number,
            place_name=place_name,
            latitude=latitude,
            longitude=longitude,
            photo=photo
        )
        return redirect("dashboard")

    return render(request, "share_location.html")

@login_required
def delete_location(request, pk):
    loc = get_object_or_404(NeedyLocation, pk=pk)
    if loc.added_by == request.user:
        loc.delete()
    return redirect('dashboard')
