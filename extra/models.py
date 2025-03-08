from django.db import models
from accounts.models import Account


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255, blank=True, null=True)
    apartment = models.CharField(max_length=255, blank=True, null=True)
    entrance = models.CharField(max_length=255, blank=True, null=True)
    floor = models.SmallIntegerField(blank=True, null=True)
    standard = models.BooleanField(default=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.street


class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='notifications/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
