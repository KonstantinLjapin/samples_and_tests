from django.urls import path
from .views import Login, Load, LogOut

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('', Load.as_view(), name='load'),
]
