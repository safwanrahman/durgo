from django.db import models

# Create your models here.


class Request(models.Model):
    path = models.TextField()
    view = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
