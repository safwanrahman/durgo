from django.db import models

# Create your models here.


class Transaction(models.Model):
    project = models.ForeignKey("organization.Project", on_delete=models.CASCADE)
    path = models.TextField()
    view = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class Segment(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()
