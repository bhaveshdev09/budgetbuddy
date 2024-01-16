from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from datetime import time, datetime, timedelta

from budget.models import Transaction
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        print(request.user)
        transaction_data = Transaction.objects.all().order_by("-created_at")
        income_data = (
            transaction_data.filter(
                transaction_type=Transaction.TRANSACTION_TYPE_INCOME
            )
            .aggregate(total_amount=models.Sum("amount", default=0))
            .get("total_amount")
        )

        expense_data = (
            transaction_data.filter(
                transaction_type=Transaction.TRANSACTION_TYPE_EXPENSE
            )
            .aggregate(total_amount=models.Sum("amount", default=0))
            .get("total_amount")
        )

        average_income_data = (
            transaction_data.filter(
                transaction_type=Transaction.TRANSACTION_TYPE_INCOME
            )
            .aggregate(total_amount=models.Avg("amount", default=0))
            .get("total_amount")
        )

        average_expense_data = (
            transaction_data.filter(
                transaction_type=Transaction.TRANSACTION_TYPE_EXPENSE
            )
            .aggregate(total_amount=models.Avg("amount", default=0))
            .get("total_amount")
        )

        return render(
            request,
            self.template_name,
            {
                "transactions": transaction_data[:5],
                "total_income_data": income_data,
                "total_expense_data": expense_data,
                "avg_income_data": average_income_data,
                "avg_expense_data": average_expense_data,
            },
        )


class DashboardAPIView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        income_data = []
        expense_data = []
        labels = []
        timerange_list = [
            (0, 3),
            (3, 6),
            (6, 9),
            (9, 12),
            (12, 15),
            (15, 18),
            (18, 21),
            (21, 0),
        ]

        transaction_data = Transaction.objects.filter(
            transaction_date=datetime.today()  # + timedelta(days=-1)
        )
        for tr in timerange_list:
            sti = (
                transaction_data.filter(
                    transaction_type="income",
                    created_at__time__range=(time(tr[0], 0), time(tr[1], 0)),
                )
                .aggregate(total_amount=models.Sum("amount", default=0))
                .get("total_amount")
            )

            ste = (
                transaction_data.filter(
                    transaction_type="expense",
                    created_at__time__range=(time(tr[0], 0), time(tr[1], 0)),
                )
                .aggregate(total_amount=models.Sum("amount", default=0))
                .get("total_amount")
            )
            income_data.append(float(sti))
            expense_data.append(-float(ste))
            labels.append(f"Hrs ({tr[0]}-{tr[1]})")

        context = {
            "income_data": income_data,
            "expense_data": expense_data,
            "labels": labels,
        }
        return JsonResponse(context, safe=True)
