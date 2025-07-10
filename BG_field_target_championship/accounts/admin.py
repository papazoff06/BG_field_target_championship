from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     model = User
#     add_form = UserCreationForm
#
#     list_display = ['pk', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
#
#