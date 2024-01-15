from django.db import models
from backend.models import BaseModel


class Transaction(BaseModel):
    TRANSACTION_TYPE_INCOME = "income"
    TRANSACTION_TYPE_EXPENSE = "expense"
    TRANSACTION_TYPE_CHOICES = (
        (TRANSACTION_TYPE_INCOME, "Income"),
        (TRANSACTION_TYPE_EXPENSE, "Expense"),
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPE_CHOICES,
        default=TRANSACTION_TYPE_EXPENSE,
    )

    def __str__(self):
        return f"{self.transaction_type} : {self.amount}"
