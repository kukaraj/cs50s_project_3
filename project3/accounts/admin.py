from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'address1', 'address2', 'password1', 'password2','city','state','zipcode')}
        ),)
    form = CustomUserChangeForm
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'address1', 'address2', 'password','city','state','zipcode')}
        ),)
    model = CustomUser
    list_display = [
    'email',
    'username',
    'password',
    'password',
    'address1',
    'address2',
	'city',
	'state',
	'zipcode']

admin.site.register(CustomUser, CustomUserAdmin)