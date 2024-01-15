# expenses/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from budget.models import Transaction
from budget.forms import IncomeForm
from django.urls import reverse_lazy


class IncomeCreateView(CreateView):
    model = Transaction
    form_class = IncomeForm
    template_name = "income_form.html"
    success_url = reverse_lazy("income_list")


class IncomeListView(ListView):
    model = Transaction
    template_name = "income_list.html"
    context_object_name = "transactions"


class IncomeDetailView(DetailView):
    model = Transaction
    template_name = "income_detail.html"
    context_object_name = "income"


class IncomeUpdateView(UpdateView):
    model = Transaction
    form_class = IncomeForm
    template_name = "income_form.html"
    success_url = reverse_lazy("income_list")
    success_message = "Income updated successfully."


class IncomeDeleteView(DeleteView):
    model = Transaction
    template_name = "income_confirm_delete.html"
    success_url = reverse_lazy("income_list")
    success_message = "Income deleted successfully."
