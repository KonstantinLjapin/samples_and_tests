from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('success')
                else:
                    auth_form.add_error('__all__', 'access denied')
            else:
                auth_form.add_error('__all__', 'access denied')
    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class LogOut(LogoutView):
    template_name = 'users/logout.html'
