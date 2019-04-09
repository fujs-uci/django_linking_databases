from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import User1CreationForm, User1ChangeForm
from .models import User1

# Register your models here.


class User1Admin(UserAdmin):
    add_form = User1CreationForm
    form = User1ChangeForm
    model = User1
    list_display = ('id', 'email', 'is_staff', 'is_active', )
    list_filter = ('id', 'email', 'is_staff', 'is_active', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_test1', 'is_test2', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_test1', 'is_test2', )}),
    )
    search_fields = ('email', )
    ordering = ('email', )


admin.site.register(User1, User1Admin)
