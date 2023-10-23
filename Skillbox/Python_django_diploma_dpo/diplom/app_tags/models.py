from django.db import models

from app_products.models import Product


class Tag(models.Model):
    product = models.ForeignKey(Product, related_name='tag', on_delete=models.CASCADE)
    tag = models.CharField(max_length=20)

    def get_url(self):
        """
        get_url
        """
        return self.tag

    class Meta:
        ordering = ["tag"]

    def __str__(self):
        """
        String object
        """
        return self.tag
