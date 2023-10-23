from django.forms import ModelForm
from .models import Article, Comment,Person


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'views_count', 'author')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('article', 'description', 'views_count', 'author')
