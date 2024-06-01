from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Account

class UserRegisterForm(UserCreationForm):
    birth_day = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # image = forms.ImageField(upload_to='accounts/media/uploads/', null=True, blank=True)
    first_name = forms.CharField(widget=forms.TextInput({'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput({'id': 'required'}))
    email = forms.EmailField(widget=forms.EmailInput({'id': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'birth_day']

    def save(self, commit=True) -> Any:
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            birth_day = self.cleaned_data.get('birth_day')
            Account.objects.create(
                user = our_user,
                birth_day = birth_day
            )
        return our_user
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'grow'
                )
            })