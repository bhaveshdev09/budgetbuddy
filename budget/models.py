from django.db import models
from backend.models import BaseModel
from django.utils import timezone
from backend import settings


class Transaction(BaseModel):
    TRANSACTION_TYPE_INCOME = "income"
    TRANSACTION_TYPE_EXPENSE = "expense"
    TRANSACTION_TYPE_CHOICES = (
        (TRANSACTION_TYPE_INCOME, "Income"),
        (TRANSACTION_TYPE_EXPENSE, "Expense"),
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, default="")
    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPE_CHOICES,
        default=TRANSACTION_TYPE_EXPENSE,
    )
    transaction_date = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.transaction_type} : {self.amount}"
