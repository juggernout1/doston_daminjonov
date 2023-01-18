from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.portfolio_view, name="justpage"),
    
]
