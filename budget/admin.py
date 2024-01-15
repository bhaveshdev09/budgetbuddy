from django.contrib import admin
from budget.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["amount", "description", "transaction_type", "transaction_date"]


admin.site.register(Transaction, TransactionAdmin)
