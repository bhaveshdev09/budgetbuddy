# expenses/forms.py
from django import forms
from budget.models import Transaction
from django.utils import timezone


class TransactionForm(forms.ModelForm):
    amount = forms.FloatField(
        initial=1.0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "autofocus": True,
                "placeholder": "Enter Amount",
            }
        ),
    )
    description = forms.CharField(
        label="Message",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Message"}
        ),
    )
    transaction_date = forms.DateField(
        label="Date",
        initial=timezone.now(),
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
            }
        ),
    )

    class Meta:
        model = Transaction
        fields = ["amount", "description", "transaction_type", "transaction_date"]


class IncomeForm(TransactionForm):
    transaction_type = forms.ChoiceField(
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
        initial=Transaction.TRANSACTION_TYPE_INCOME,
        label="",
        widget=forms.Select(attrs={"class": "form-control", "hidden": True}),
    )


class ExpenseForm(TransactionForm):
    transaction_type = forms.ChoiceField(
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
        initial=Transaction.TRANSACTION_TYPE_EXPENSE,
        label="",
        widget=forms.Select(attrs={"class": "form-control", "hidden": True}),
    )
