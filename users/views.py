from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from users.forms import CustomUserForm, CustomUserAuthForm
from django.views.generic import View
from .models import User


# Authentication
class CustomRegisterView(FormView):
    form_class = CustomUserForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("dashboard")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        form.save(commit=True)
        user = authenticate(self.request, email=email, password=password)
        print(user)

        if user is not None:
            login(self.request, user)
            # Your custom logic after successful login
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(form.errors.as_data())
        response = super().form_invalid(form)
        return response


class CustomLoginView(FormView):
    form_class = CustomUserAuthForm
    template_name = "auth/login.html"
    success_url = reverse_lazy("dashboard")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            # Your custom logic after successful login
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(form.errors.as_data())
        response = super().form_invalid(form)
        return response


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
