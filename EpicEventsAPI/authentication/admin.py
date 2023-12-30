from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email',
                    'first_name', 'last_name', 'department']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('department',)}),
    )


admin.site.register(User, CustomUserAdmin)
