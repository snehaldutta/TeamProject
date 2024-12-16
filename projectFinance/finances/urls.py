from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.submitEntry, name='submitEntry'),
    path("data/", views.fetch_expenses, name='fetchData'),
    path("dashboard/", views.graphs_expenses, name='graphsExpenses')
]