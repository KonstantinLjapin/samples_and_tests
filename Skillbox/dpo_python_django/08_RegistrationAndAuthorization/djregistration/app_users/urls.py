from django.urls import path
from .views import Login, LogOut, UsersList, RegView, BillList, RegBillView

urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('registr/', RegView.as_view(), name='reg'),
    path('bills/', BillList.as_view(), name='bills'),
    path('bill_reg/', RegBillView.as_view(), name='bill_reg'),
]
