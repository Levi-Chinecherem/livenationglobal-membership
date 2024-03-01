# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)


# # accounts/admin.py
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
#     search_fields = ('email', 'username', 'first_name', 'last_name')
#     ordering = ('email',)

# admin.site.register(CustomUser, CustomUserAdmin)
