from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "avatar", "password1", "password2"]

