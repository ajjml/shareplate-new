from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home_page,name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('share_food/',views.share_food_view,name='share_food'),
    path("delete_food/<int:pk>/", views.delete_food, name="delete_food"),
    path("share_location/", views.share_location, name="share_location"),
    path("delete_location/<int:pk>/", views.delete_location, name="delete_location"),
        # Forgot password / Reset password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='forgot_password.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),


    ]
