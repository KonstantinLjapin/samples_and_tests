from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import DetailView
from .models import NewsItem
from django.core import serializers
from  django.contrib.sitemaps import Sitemap


def get_news(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, NewsItem.objects.all())
    return HttpResponse(data)


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'news_d.html'


class SiteMap(Sitemap):
    changefreq = 'weekly'
    priority =0.9

    def items(self):
        return NewsItem.objects.filter(is_published=True).all()

    def lastmod(self, obj: NewsItem):
        return obj.published_at

