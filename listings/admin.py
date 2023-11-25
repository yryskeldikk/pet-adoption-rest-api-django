from django.contrib import admin
from .models import Pet
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class PetAdmin(admin.ModelAdmin):
        list_display = ('name','id')

admin.site.register(Pet, PetAdmin)

