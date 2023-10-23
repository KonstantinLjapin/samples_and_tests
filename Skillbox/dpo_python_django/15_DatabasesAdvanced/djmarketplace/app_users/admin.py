from django.contrib import admin
from .models import Product, Person, Mall

admin.site.register(Mall)
admin.site.register(Person)
admin.site.register(Product)
