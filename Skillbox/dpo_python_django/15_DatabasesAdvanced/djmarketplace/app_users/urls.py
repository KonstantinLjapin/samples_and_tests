from .views import Login, LogOut, UsersList, RegView, ProductList, RegProductView
from django.urls import path
import debug_toolbar

urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('registr/', RegView.as_view(), name='reg'),
    path('product/', ProductList.as_view(), name='product'),
    path('buy_product/', RegProductView.as_view(), name='buy_product'),
]
