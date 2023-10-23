from django.db import models
from django.contrib.auth.models import User


class Bill(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='price', default=0)
    views_count = models.IntegerField(verbose_name='views count', default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bill'
        permissions = (
            ("can_masscreate_tag", "Can mass create Tag"),
        )
