from django.db import models
from django.conf import settings


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=512, db_index=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    event_time = models.DateTimeField()
    body = models.TextField()
    tags = models.ManyToManyField('Tag')
    handled = models.BooleanField(default=False)

    # @property
    # def place_name(self):
    #     return self.place.place_name

    def __str__(self):
        return self.title
      
      
class Tag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
      
      
class Place(models.Model):
    place_name = models.CharField(max_length=512)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_number = models.CharField(max_length=16)
    office_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.place_name


class User(models.Model):
    external_id = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    creation_date = models.DateTimeField()
    tags = models.ManyToManyField('Tag')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Notification(models.Model):
    status_send = models.BooleanField(default=False)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
