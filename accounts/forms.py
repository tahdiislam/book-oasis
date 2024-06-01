from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Account

class UserRegisterForm(UserCreationForm):
    balance = forms.DecimalField(default=0, max_digits=12, decimal_places=2)
    birth_day = forms.DateField(null=True, blank=True)
    image = forms.ImageField(upload_to='accounts/media/uploads/', null=True, blank=True)