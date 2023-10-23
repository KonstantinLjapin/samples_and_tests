from django.contrib import admin
from .models import Tag

admin.site.register(Tag)

# Register your models here.


class TagInline(admin.TabularInline):
    fk_name = 'product'
    model = Tag
