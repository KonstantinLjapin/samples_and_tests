from django.contrib import admin

from .models import Person, Article, Comment

admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Article)
