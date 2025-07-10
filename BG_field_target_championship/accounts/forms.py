from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ShooterRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Your password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm your password'}),
        }