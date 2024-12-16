from django.contrib import admin
from .models import ExpensesTracker, DailyBudgetLimit
# Register your models here.
admin.site.register(ExpensesTracker)
admin.site.register(DailyBudgetLimit)