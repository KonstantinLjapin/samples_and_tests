from django.db import models
from django.contrib.auth.models import User


class Mall(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'mall'
        verbose_name_plural = 'shops'
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    mall = models.ForeignKey(Mall, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['title']


class Person(User):
    name = models.CharField(max_length=30)
    wallet = models.PositiveIntegerField()
    card = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'buyer'
        verbose_name_plural = 'buyer'
        ordering = ['name']
