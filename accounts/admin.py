from django.contrib import admin
from .models import ShopUser
from django.contrib.auth.admin import UserAdmin


@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):
    model = ShopUser
    list_display = ('email', 'is_staff', 'is_active', 'is_seller')

