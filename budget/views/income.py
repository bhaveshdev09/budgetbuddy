# expenses/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from budget.models import Transaction
from budget.forms import IncomeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = IncomeForm
    template_name = "income_form.html"
    success_url = reverse_lazy("income_list")

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class IncomeListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "income_list.html"
    context_object_name = "transactions"
    paginate_by = 5
    queryset = Transaction.objects.filter(
        transaction_type=Transaction.TRANSACTION_TYPE_INCOME
    ).order_by("-created_at")


class IncomeDetailView(DetailView):
    model = Transaction
    template_name = "income_detail.html"
    context_object_name = "income"


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = IncomeForm
    template_name = "income_form.html"
    success_url = reverse_lazy("income_list")
    success_message = "Income updated successfully."


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = "income_confirm_delete.html"
    success_url = reverse_lazy("income_list")
    success_message = "Income deleted successfully."
