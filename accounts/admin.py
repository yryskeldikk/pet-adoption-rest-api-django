from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
        list_display = ('username', 'email','id')

admin.site.register(Account, UserAdmin)