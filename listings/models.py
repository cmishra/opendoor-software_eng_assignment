from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class House(models.Model):
    id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sq_ft = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()