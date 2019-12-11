from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=512, db_index=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    event_time = models.DateTimeField()
    body = models.TextField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Place(models.Model):
    pass


class Tag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
