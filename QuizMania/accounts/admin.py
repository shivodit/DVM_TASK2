from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
        'role',
    ]

