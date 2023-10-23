from django.contrib import admin
from .models import Product, Review, Specifications, Picture
from app_tags.admin import TagInline

admin.site.register(Review)
admin.site.register(Picture)
admin.site.register(Specifications)
# Register your models here.


class PictureInline(admin.TabularInline):
    fk_name = 'product'
    model = Picture


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline, TagInline,]