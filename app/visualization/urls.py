from django.urls import path
from visualization import views

app_name = "visualization"

urlpatterns = [
    path("", views.index),
]