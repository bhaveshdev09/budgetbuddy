# expenses/urls.py
from django.urls import path
from django.views.generic import TemplateView
from users.views import CustomLoginView, CustomLogoutView, CustomRegisterView

urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
