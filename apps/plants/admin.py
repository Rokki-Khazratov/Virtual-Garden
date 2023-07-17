from django.contrib import admin
from .models import Plants,UserProfile

@admin.register(Plants)
class PlantsAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_per_page = 20

    class Meta:
        model = Plants

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','id']
    list_per_page = 20

    class Meta:
        model = UserProfile