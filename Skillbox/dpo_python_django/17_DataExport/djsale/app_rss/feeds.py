from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from .models import NewsItem
"""any model"""
from django.urls import reverse


class LatesNewsFeed(Feed):
    title = "News"
    link = "/sitenews/"
    description = "news"

    def item(self) -> QuerySet:
        return NewsItem.objects.order_by('published_at')[:5]

    def item_title(self, item: NewsItem) -> str:
        return item.title

    def item_description(self, item: NewsItem) -> str:
        return item.descriptions

    def  item_link(self, item: NewsItem) -> str:
        return reverse('news-item', args=[item.pk])
