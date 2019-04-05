from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserRegisterForm, UserChangeForm
from accounts.models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserRegisterForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('usuario', 'roles', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'roles')
    fieldsets = (
        (None, {'fields': ('usuario', 'password', 'password1', 'password2')}),
        ('Personal info', {'fields': ('nome', 'credencial', )}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usuario', 'roles', 'password1', 'password2')}),
    )
    search_fields = ('usuario', )
    ordering = ('usuario',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
