from django.contrib.auth.views import LogoutView
from django.urls import path

from BG_field_target_championship.accounts import views

urlpatterns = [
    path('register/', views.ShooterRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]