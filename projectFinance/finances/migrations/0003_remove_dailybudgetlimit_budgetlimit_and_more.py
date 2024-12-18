# Generated by Django 5.1.3 on 2024-12-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0002_dailybudgetlimit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dailybudgetlimit",
            name="budgetLimit",
        ),
        migrations.AddField(
            model_name="dailybudgetlimit",
            name="budget_limit",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="dailybudgetlimit",
            name="percentage_spent",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="dailybudgetlimit",
            name="total_spent",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="dailybudgetlimit",
            name="date",
            field=models.DateField(),
        ),
    ]
