from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext


class MainView(View):

    def get(self, request):
        return render(request, 'main.html')