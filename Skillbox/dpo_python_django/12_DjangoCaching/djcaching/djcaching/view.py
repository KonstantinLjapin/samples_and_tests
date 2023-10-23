from django.shortcuts import render
from django.views.decorators.cache import cache_page
from time import sleep
from .models import AbstractModel
from django.core.cache import cache
@cache_page(30)
def abstract(request, *args, **kwargs):
    sleep(5)
    abs = AbstractModel.objects.all()
    some_cashe = {some: abstract}
    cache.set_many(some_cashe)
    return render(request, 'abstract.html', context={
        'abs': abs
    })
