from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    licence = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.make}, {self.model}'

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.TextField(max_length=200)
    service_price = models.IntegerField
    service_duration = models.CharField(max_length=20)

    def __str__(self):
        return self.service_name

class Location(models.Model):
    address = models.TextField(max_length=200)
    opening_hrs = models.CharField(max_length=50)

    def __str__(self):
        return self.address

class Request(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Order(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    complete = models.BooleanField
    confirmed = models.BooleanField
