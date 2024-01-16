# expenses/urls.py
from django.urls import path
from budget.views import (
    IncomeCreateView,
    IncomeListView,
    IncomeDetailView,
    IncomeUpdateView,
    IncomeDeleteView,
    ExpenseCreateView,
    ExpenseListView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    DashboardView,
    DashboardAPIView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("api/transc/", DashboardAPIView.as_view(), name="dashboard-bar-api"),
    # CRUD for Income
    path("income/add/", IncomeCreateView.as_view(), name="income_create"),
    path("income/", IncomeListView.as_view(), name="income_list"),
    path("income/<int:pk>/update/", IncomeUpdateView.as_view(), name="income_update"),
    path("income/<int:pk>/delete/", IncomeDeleteView.as_view(), name="income_delete"),
    # CRUD for Expense
    path("expense/add/", ExpenseCreateView.as_view(), name="expense_create"),
    path("expense/", ExpenseListView.as_view(), name="expense_list"),
    path(
        "expense/<int:pk>/update/", ExpenseUpdateView.as_view(), name="expense_update"
    ),
    path(
        "expense/<int:pk>/delete/", ExpenseDeleteView.as_view(), name="expense_delete"
    ),
]
