from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(verbose_name='views count', default=0)
    author = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'comment'


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, default=None)

    def __str__(self):
        return self.name

