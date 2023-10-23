from django.db import models


class AbstractModel(models.Model):
    a = models.CharField(max_length=10)
    b = models.IntegerField(max_length=10)
