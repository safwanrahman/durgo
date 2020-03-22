from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100)
    icon = models.ImageField(blank=True, null=True)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
