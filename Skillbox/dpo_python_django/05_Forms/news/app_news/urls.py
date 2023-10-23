from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassBasedView.as_view()),
    path('article',  views.AuthorCreate.as_view(), name='article'),
    path('comment',  views.AuthorCommentUpdate.as_view(), name='comment'),
]
