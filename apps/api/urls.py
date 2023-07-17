from django.urls import path
from apps.api import APIviews

urlpatterns = [
    path('plants/',APIviews.plant_list_create_view),
    path('plant/<int:pk>',APIviews.plant_detail_view),
    path('plant/<int:pk>/update',APIviews.plant_update_view),
    path('plant/<int:pk>/delete',APIviews.plant_delete_view),

    path('user/<int:id>',APIviews.profile_list_view)
]