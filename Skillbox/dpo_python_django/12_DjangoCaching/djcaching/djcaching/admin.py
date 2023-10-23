from django.contrib import admin
from .models import AbstractModel


class NewsAbstractAdmin(admin.ModelAdmin):
    list_display = ['id', 'a']


admin.site.register(AbstractModel, NewsAbstractAdmin)

