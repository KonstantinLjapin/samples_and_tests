from django.urls import path
from .views import login_view, AnotherLoginView, LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
