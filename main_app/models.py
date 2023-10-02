from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    licence = models.CharField(max_length=10)

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.TextField(max_length=200)
    service_price = models.IntegerField
    service_duration = models.CharField(max_length=20)

class Request(models.Model):
    address = models.TextField(max_length=200)
    opening_hrs = models.CharField(max_length=50)
