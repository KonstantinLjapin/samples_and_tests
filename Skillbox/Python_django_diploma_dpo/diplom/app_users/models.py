from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=160, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username
