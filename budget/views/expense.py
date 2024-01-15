# expenses/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from budget.models import Transaction
from budget.forms import ExpenseForm
from django.urls import reverse_lazy


class ExpenseCreateView(CreateView):
    model = Transaction
    form_class = ExpenseForm
    template_name = "expense_form.html"
    success_url = reverse_lazy("expense_list")

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class ExpenseListView(ListView):
    model = Transaction
    template_name = "expense_list.html"
    context_object_name = "transactions"
    paginate_by = 5
    queryset = Transaction.objects.filter(
        transaction_type=Transaction.TRANSACTION_TYPE_EXPENSE
    ).order_by("-created_at")


class ExpenseDetailView(DetailView):
    model = Transaction
    template_name = "expense_detail.html"
    context_object_name = "expense"


class ExpenseUpdateView(UpdateView):
    model = Transaction
    form_class = ExpenseForm
    template_name = "expense_form.html"
    success_url = reverse_lazy("expense_list")
    success_message = "expense updated successfully."


class ExpenseDeleteView(DeleteView):
    model = Transaction
    template_name = "expense_confirm_delete.html"
    success_url = reverse_lazy("expense_list")
    success_message = "expense deleted successfully."
