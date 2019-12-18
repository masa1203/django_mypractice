# users/admin.py

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """    add_form_template = None
        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            (_('Personal info'), {'fields': ('first_name', 'last_name')}),
            (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )
        add_fieldsets = (
            (None, {
                'classes': ('wide', ),
                'fields': ('email', 'password1', 'password2'),
            }),
        )"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email', 'username', 'is_staff', 'age', 'weight']
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email', )


admin.site.register(CustomUser, CustomUserAdmin)
