from django.shortcuts import render
from django.contrib import messages
from .models import ExpensesTracker, DailyBudgetLimit
from django.db.models import Sum
import json
from decimal import Decimal
import os 


# Function to handle submitting new expenses
def submitEntry(request):
    if request.method == 'POST':
        print(request.POST)  # For debugging
        print(request.FILES)
        date = request.POST.get('date')
        amount = float(request.POST.get('amount'))  # Convert amount to float for calculations
        description = request.POST.get('description')
        category = request.POST.get('category')
        budget_limit = request.POST.get('budget_limit')
        uploaded_file = request.FILES.get('bill_image')
        # Create new transaction
        ExpensesTracker.objects.create(
            date=date,
            amount=amount,
            description=description,
            category=category,
            bill_image=uploaded_file
        )

        # Check if budget_limit is provided for the category
        if budget_limit:
            # Convert budget_limit to float and store it in the DailyBudgetLimit model
            budget_limit = float(budget_limit)

            # Check if category exists in DailyBudgetLimit
            category_budget, created = DailyBudgetLimit.objects.update_or_create(
                cate=category,
                defaults={'budget_limit': Decimal(budget_limit)}  # Update the budget limit if category exists
            )

            if created:
                messages.success(request, f"Budget limit for category '{category}' has been set to {budget_limit}.")

        try:
            # Retrieve the stored budget limit for this category
            category_budget = DailyBudgetLimit.objects.get(cate=category)
            print("Category Budget:", category_budget)  # Debugging
            total_expenses = ExpensesTracker.objects.filter(category=category).aggregate(total_spent=Sum('amount'))['total_spent'] or 0.0
            print("Total Expenses:", total_expenses)  # Debugging
        except DailyBudgetLimit.DoesNotExist:
            category_budget = None
            total_expenses = 0
            messages.warning(request, f"No budget limit found for category: {category}")

        # Convert total_expenses to Decimal for comparison with Decimal budget_limit
        total_expenses = Decimal(total_expenses)  # Convert to Decimal

        # Convert 0.7 to Decimal for multiplication with the Decimal budget limit
        threshold = Decimal(0.7) * category_budget.budget_limit

        # Check if the total expenses exceed 70% of the budget
        if category_budget and total_expenses > threshold:
            message = f"Warning: Your expenses in the '{category}' category have exceeded 70% of the budget!"
            messages.warning(request, message)
        else:
            messages.success(request, "Expense added successfully!")

        # Success message
        messages.success(request, 'Transaction added successfully!')

    return render(request, 'finances/index.html')


# Function to fetch expenses data
def fetch_expenses(request):
    expenses = ExpensesTracker.objects.all().order_by('-date')

    params = {
        'expenses': expenses
    }

    return render(request, 'finances/data.html', params)


# Custom JSON encoder for Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


# Function to fetch and return data for graphs
def graphs_expenses(request):
    data = ExpensesTracker.objects.values('category').annotate(totalValue=Sum('amount')).order_by('-totalValue')
    labels = [item['category'] for item in data]
    values = [item['totalValue'] for item in data]

    # Prepare the data to be rendered into the template as JSON
    contents = {
        'labels_json': json.dumps(labels, cls=DecimalEncoder),
        'values_json': json.dumps(values, cls=DecimalEncoder)
    }

    return render(request, 'finances/dashboard.html', contents)