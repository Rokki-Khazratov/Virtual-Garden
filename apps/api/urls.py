from django.urls import path
from apps.api import APIviews

urlpatterns = [
    path('plants/',APIviews.plant_list_create_view),
    path('plant/<int:pk>',APIviews.plant_detail_view),
    path('plant/<int:pk>/update',APIviews.plant_update_view),
    path('plant/<int:pk>/delete',APIviews.plant_delete_view),

    path('user/<int:id>',APIviews.profile_list_view), # user json
    #? path = user/<int:id>?plants=true PLANTS IN USER.PLANTS json 

    path('user/<int:id>/cart/add/', APIviews.UserProfileCartAddView.as_view(), name='add-to-cart'),
    path('user/<int:id>/cart/delete/<int:plant_id>/', APIviews.UserProfileCartDeleteView.as_view(), name='remove-from-cart'),

]