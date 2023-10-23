from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', blank=True)
    href = models.CharField(max_length=20)

    class Meta:
        ordering = ["title"]

    def __str__(self):

        return self.title


class Subcategories(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)


