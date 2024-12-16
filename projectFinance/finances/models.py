from django.db import models
from datetime import date

# Create your models here.
class ExpensesTracker(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    date = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    bill_image = models.ImageField(upload_to='bill_images/',null=True,blank=True)

    def __str__(self):
        return f"{self.date} - {self.description} ({self.category})"

class DailyBudgetLimit(models.Model):
    cate = models.CharField(max_length=100, default='General')
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cate} - {self.budget_limit}"