from django.contrib import admin
from .models import Plants,UserProfile

admin.site.register(Plants)

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','id']
    list_per_page = 20

    class Meta:
        model = UserProfile