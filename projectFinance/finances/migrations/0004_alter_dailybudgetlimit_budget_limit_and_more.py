# Generated by Django 5.1.3 on 2024-12-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0003_remove_dailybudgetlimit_budgetlimit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailybudgetlimit",
            name="budget_limit",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="dailybudgetlimit",
            name="category",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="dailybudgetlimit",
            name="percentage_spent",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="dailybudgetlimit",
            name="total_spent",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
