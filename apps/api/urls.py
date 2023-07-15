from django.urls import path
from apps.api import APIviews

urlpatterns = [
    path('plants/',APIviews.plant_list_create_view)
]