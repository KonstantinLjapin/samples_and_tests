from django.urls import path
from .feeds import LatesNewsFeed


urlpatterns = [
   path('lates/feed/', LatesNewsFeed())
]