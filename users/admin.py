from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User

from .forms import CustomUserChangeForm, CustomUserCreationForm, GroupAdminForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)

        return ' '.join(groups)

    group.short_description = 'Groups'

    list_display = ('email', 'first_name', 'last_name', 'PRN',
                    'year', 'branch', 'division', 'is_staff', 'is_active', 'date_joined', 'group')
    list_filter = ('email', 'first_name', 'last_name', 'PRN', 'year', 'branch', 'division',
                   'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name',
                           'last_name', 'PRN', 'year', 'branch', 'division')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name',
                       'last_name', 'PRN', 'year', 'branch', 'division', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Unregister the original Group admin.
admin.site.unregister(Group)


admin.site.register(User, CustomUserAdmin)

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
