from django.urls import path
from .views import get_news, NewsDetailView

urlpatterns = [
    path('', get_news, name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_item')
]