# Generated by Django 5.0 on 2024-01-15 11:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
