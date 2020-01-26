from abc import ABC
from rest_framework.authtoken.models import Token

from rest_framework import serializers

from handler.models import Event, Place, Tag, User as AppUser
from django.contrib.auth.models import User


class EventsSerializer(serializers.ModelSerializer):
    place_name = serializers.SerializerMethodField(read_only=True)
    event_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ['title', 'place', 'body', 'event_date', 'place_name', 'event_time']

    def get_place_name(self, obj):
        return f'{obj.place.place_name}'

    def get_event_date(self, obj):
        event_date = obj.event_time.strftime("%Y.%m.%d %H:%M")
        return event_date


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PrivatePlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class PrivateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
