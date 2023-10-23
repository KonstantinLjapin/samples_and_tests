from django.db import models


class Bill(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='price', default=0)
    views_count = models.IntegerField(verbose_name='views count', default=0)
    author = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bill'


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, default=None)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
