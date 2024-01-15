# expenses/forms.py
from django import forms
from budget.models import Transaction


class IncomeForm(forms.ModelForm):
    transaction_type = forms.ChoiceField(
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
        initial=Transaction.TRANSACTION_TYPE_EXPENSE,
        label="",
        widget=forms.Select(attrs={"class": "form-control", "hidden": True}),
    )
    amount = forms.FloatField(
        initial=1.0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "autofocus": True,
            }
        ),
    )
    description = forms.CharField(
        label="message",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Transaction
        fields = ["amount", "description", "transaction_type"]
