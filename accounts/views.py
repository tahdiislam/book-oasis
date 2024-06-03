from django.shortcuts import render
from .forms import UserRegisterForm
from django.views.generic import FormView, View, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'User successfully register and login')
        return super().form_valid(form)

class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self) -> str:
        messages.success(self.request, f'Welcome Back {self.request.user.first_name} {self.request.user.last_name}')
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class DepositMoney()