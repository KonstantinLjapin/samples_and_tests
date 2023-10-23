from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="media/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bill'
