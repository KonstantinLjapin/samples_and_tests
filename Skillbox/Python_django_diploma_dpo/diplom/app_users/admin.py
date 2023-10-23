from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class RecordAdmin(admin.ModelAdmin):
    list_per_page = 200


admin.site.register(CustomUser, RecordAdmin)
