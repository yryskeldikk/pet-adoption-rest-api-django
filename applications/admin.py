from django.contrib import admin
from .models import Applications


# Register your models here.
class ApplicationsAdmin(admin.ModelAdmin):
        list_display = ('applicant', 'pet','id')

admin.site.register(Applications, ApplicationsAdmin)