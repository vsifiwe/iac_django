from django.db import models

# Create your models here.

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    district = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    road_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Device(models.Model):
    device_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()

class Appointments(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return super().__str__()