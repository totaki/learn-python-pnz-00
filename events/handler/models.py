from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=512)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_number = models.IntegerField()
    office_number = models.IntegerField()

    def __str__(self):
        return self.place_name
