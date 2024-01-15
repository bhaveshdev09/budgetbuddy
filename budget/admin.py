from django.contrib import admin
from budget.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["amount", "description"]


admin.site.register(Transaction, TransactionAdmin)
