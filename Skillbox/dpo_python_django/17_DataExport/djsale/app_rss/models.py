from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=120, verbose_name='title')
    text = models.TextField(verbose_name='text')
    is_published = models.BooleanField(default=False)
    type = models.ForeignKey('NewsType', on_delete=models.CASCADE, related_name='news', null=True)
    descriptions = models.TextField(verbose_name='des', default='')
    published_at = models.DateTimeField(verbose_name='data_pub', null=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


class NewsType(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')
    code = models.CharField(max_length=64, verbose_name='code')

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name

