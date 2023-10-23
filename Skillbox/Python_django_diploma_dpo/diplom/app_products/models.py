#TODO specifications model
from django.db import models
from datetime import datetime
from django.urls import reverse
from app_users.models import CustomUser
from app_categories.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    count = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    fullDescription = models.TextField(blank=True)
    href = models.CharField(max_length=20, blank=True)
    freeDelivery = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        """
        String object
        """
        return self.title


class Picture(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True, editable=True)

    def get_url(self):
        """
        get_url
        """
        return self.images.url

    class Meta:
        ordering = ["images"]

    def __str__(self):
        """
        String object
        """
        return self.images.url


class Review(models.Model):
    author = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    rate = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["text"]

    def __str__(self):

        return self.text


class Specifications(models.Model):
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    value = models.CharField(max_length=4, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """
        String object
        """
        return self.name
