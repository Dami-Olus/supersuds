from django.contrib import admin

# Register your models here.
from .models import Car, Service, Location, Request

admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Location)
admin.site.register(Request)