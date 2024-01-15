# expenses/urls.py
from django.urls import path
from budget.views import (
    IncomeCreateView,
    IncomeListView,
    IncomeDetailView,
    IncomeUpdateView,
    IncomeDeleteView,
)

urlpatterns = [
    # ... your existing URLs
    # CRUD for Income
    path("income/add/", IncomeCreateView.as_view(), name="income_create"),
    path("income/", IncomeListView.as_view(), name="income_list"),
    path("income/<int:pk>/update/", IncomeUpdateView.as_view(), name="income_update"),
    path("income/<int:pk>/delete/", IncomeDeleteView.as_view(), name="income_delete"),
]
