from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=512)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_number = models.CharField(max_length=16)
    office_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.place_name
